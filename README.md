# Open AI Desktop Assistant

## About
This project is an AI-powered desktop assistant that allows users to interact with an AI through voice commands. The assistant can take screenshots of the user's desktop, enabling it to provide context-aware responses. It is built on Python and utilizes the OpenAI API.

## Features
- Voice interaction with AI.
- Context-aware responses by taking screenshots.
- Customizable settings through `.env` file.
- Sounds for different interactions.

## Prerequisites
- Python 3.8+
- Pip for installing packages

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/pauliusdotpro/open-ai-desktop-assist
   ```
2. Navigate to the cloned directory:
   ```
   cd open-ai-desktop-assist
   ```
3. Install required packages:
   ```
   pip install -r requirements.txt
   ```
4. Rename `.env.example` to `.env` and setup with your OpenAI API key

## Usage

1. Run the application:
   ```
   python app.py
   ```
2. Use the default hotkey `Ctrl+Shift` to activate the assistant.
3. Speak your command, and the assistant will take a screenshot and provide a response.

## Customization
- Edit the `.env` file to change settings like hotkey, voice, and sounds.

## Contributing
Contributions are welcome! If you have ideas for improvements or bug fixes, feel free to:

1. Fork the repository.
2. Create a new branch for your feature.
3. Commit your changes.
4. Push to the branch.
5. Open a pull request.

Please ensure your code adheres to the project's coding style and include tests for new features.

## License
This project is open-sourced under the [GNU GPLv3 license](LICENSE.md).

## Support
For support, open an issue or submit a pull request.
