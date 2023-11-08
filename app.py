import pyautogui
import base64
import requests
from openai import OpenAI
import pygame
import speech_recognition as sr
import keyboard
import os
from dotenv import load_dotenv

load_dotenv()
language = os.getenv('LANGUAGE') 
api_key = os.getenv('API_KEY')
voice = os.getenv('VOICE')
hotkey = os.getenv('HOTKEY')

hello_sound = os.getenv('HELLO_SOUND')
thinking_sound = os.getenv('THINKING_SOUND')
got_it_sound = os.getenv('GOT_IT_SOUND')
repeat_sound = os.getenv('REPEAT_SOUND')

system_message = f"Provide VERY short and VERY consice answers! Answer in {language} language."

chat_history = []

pygame.mixer.init()
client = OpenAI(api_key=api_key)
r = sr.Recognizer()

def take_screenshot_base64():
	im1 = pyautogui.screenshot()
	im1.save("screenshot.png")
	with open("screenshot.png", "rb") as image_file:
		encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
	return encoded_string

def get_vision(base64_image, query="What's in this image?"):
	headers = {
		"Content-Type": "application/json",
		"Authorization": f"Bearer {api_key}"
	}

	messages = []

	messages.append({
		"role": "system",
		"content": [
			{
				"type": "text",
				"text": system_message
			}
		]
	})

	for chat in chat_history:
		messages.append(chat)

	messages.append({
		"role": "user",
		"content": [
			{
				"type": "text",
				"text": query
			},
			{
				"type": "image_url",
				"image_url": {
				"url": f"data:image/jpeg;base64,{base64_image}"
				}
			}
		]
	})

	payload = {
		"model": "gpt-4-vision-preview",
		"messages": messages,
		"max_tokens": 300
	}

	response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
	return response

def text_to_speech(text, output_file="sounds/output.mp3"):
	response = client.audio.speech.create(
		model="tts-1",
		voice=voice,
		input=text,
	)

	response.stream_to_file(output_file)

def play_sound(input_file="sounds/output.mp3"):
	pygame.mixer.music.load(input_file)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy():
		pygame.time.Clock().tick(10)
	pygame.mixer.music.unload()

def get_speech_to_text():
	with sr.Microphone() as source:
		print("Listening for input!")
		audio_data = r.listen(source)
		# Change to whisper
		text = r.recognize_google(audio_data)

		return text

def main_logic():
	try:
		print('Shift + Ctrl is pressed. Starting to listen for input.')
		text = get_speech_to_text()
		print(f"Input: {text}")
		base64_image = take_screenshot_base64()
		print("Took screenshot!")
		play_sound(thinking_sound)
		response = get_vision(base64_image, text)
		print("Got response!")
		messageResponse = response.json()['choices'][0]['message']['content']
		print(f"Response: {messageResponse}")

		chat_history.append({
			"role": "user",
			"content": [
				{
				"type": "text",
				"text": text
				},
				{
					"type": "image_url",
					"image_url": {
					"url": f"data:image/jpeg;base64,{base64_image}"
					}
				}
			]
		})

		chat_history.append({
			"role": "assistant",
			"content": [
				{
					"type": "text",
					"text": messageResponse
				}
			]
		})

		print("Text to speech time!")
		text_to_speech(messageResponse)
		play_sound(got_it_sound)
		print("Playing sound!")
		play_sound()
		print("Done!")
	except Exception as e:
		print(e)
		print("Something went wrong!")
		play_sound(repeat_sound)

play_sound(hello_sound)
keyboard.add_hotkey(hotkey, main_logic)
keyboard.wait()