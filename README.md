# personal_voice_chat_bot
A voice chat bot that reponds to any questions regarding myself.

# Personal Voice Bot

This is a voice-enabled chatbot that uses ChatGPT to answer questions about you. The bot can:
1. Record your voice input
2. Convert speech to text
3. Process questions using ChatGPT
4. Respond with synthesized speech

## Setup

Presetup - Clone the repository and cd into folder.

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

3. Make sure you have a working microphone connected to your computer.

## Usage

1. Run the voice bot:
```bash
python voice_bot.py
```

2. When prompted, speak your question clearly into the microphone.

3. The bot will:
   - Record your voice (5 seconds by default)
   - Convert it to text
   - Process it with ChatGPT
   - Respond with synthesized speech

4. Press Ctrl+C to exit the program.

## Customization

You can modify the following parameters in `voice_bot.py`:
- Recording duration (default: 8 seconds)
- Speech rate (default: 150)
- Voice volume (default: 0.9)

## Example Questions

The bot can answer various questions about you, such as:
- What should we know about your life story in a few sentences?
- What's your #1 superpower?
- What are the top 3 areas you'd like to grow in?
- What misconception do your coworkers have about you?
- How do you push your boundaries and limits?

## Requirements

- Python 3.7+
- Working microphone
- Internet connection
- OpenAI API key

## Output
![image](https://github.com/user-attachments/assets/432bbc27-f15d-45f6-8aea-ca1470df940e)

The output is converted into speech.
