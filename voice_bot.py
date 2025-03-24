import os
import speech_recognition as sr
import pyttsx3
import openai
from dotenv import load_dotenv
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import time
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 150)    #Speed of speech
engine.setProperty('volume', 0.9)  #Volume level

#Load personal information
def load_personal_info(file_path="personal_info.txt"):
    """Load personal information from a text file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Warning: {file_path} not found. Using default context.")
        return "You are a helpful AI assistant that answers questions about the user. Keep responses concise and natural."

PERSONAL_INFO = load_personal_info()
conversation_history = [
    {"role": "system", "content": PERSONAL_INFO}
]

def record_audio(duration=8, sample_rate=44100):
    """Record audio from microphone"""
    print("Recording... (8 seconds)")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype=np.int16)
    sd.wait()
    print("Recording finished")
    return recording

def save_audio(recording, filename="temp.wav", sample_rate=44100):
    """Save recorded audio to WAV file"""
    recording = (recording * 32767).astype(np.int16)
    wav.write(filename, sample_rate, recording)

def speech_to_text(audio_file):
    """Convert speech to text using Google Speech Recognition"""
    try:
        with sr.AudioFile(audio_file) as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5) #adjust for ambient noise
            audio = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio)
                return text
            except sr.UnknownValueError:
                return "Could not understand audio"
            except sr.RequestError:
                return "Could not request results"
    except Exception as e:
        print(f"Error in speech_to_text: {str(e)}")
        return "Error processing audio file"

def get_chatgpt_response(question):
    """Get response from ChatGPT using personal information and conversation history"""
    try:
        # Add the new question to conversation history
        conversation_history.append({"role": "user", "content": question})
        
        # Get response from ChatGPT
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation_history
        )
        
        response_content = response.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": response_content})
        
        return response_content
    except Exception as e:
        return f"Error getting response: {str(e)}"

def text_to_speech(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def main():
    print("Voice Bot is ready! Press Ctrl+C to exit.")
    print("Using personal information from personal_info.txt")
    print("You have 8 seconds to speak your question.")
    
    while True:
        try:
            # Record audio
            recording = record_audio()
            # Save audio to file
            save_audio(recording)
            # Convert speech to text
            question = speech_to_text("temp.wav")
            print(f"You asked: {question}")
            # Get response from ChatGPT
            response = get_chatgpt_response(question)
            print(f"Bot response: {response}")
            # Convert response to speech
            text_to_speech(response)
            # Clean up temporary file
            if os.path.exists("temp.wav"):
                os.remove("temp.wav")
                
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            continue

if __name__ == "__main__":
    main() 