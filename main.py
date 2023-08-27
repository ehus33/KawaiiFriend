"""import speech_recognition as sr
import pyttsx3
import openai
from constants import openai_api_key
from constants import twilio_account_sid
from constants import twilio_auth_token
from constants import twilio_phone_number
# Set up the OpenAI API with your API key
openai.api_key = openai_api_key

account_sid = twilio_account_sid
auth_token = twilio_auth_token
phone_number = twilio_phone_number

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
            return None

def speak(text):
    engine.say(text)
    engine.runAndWait()

def send_sms(to_number, message):
    twilio_client.messages.create(
        to=to_number,
        from_=twilio_phone_number,
        body=message
    )

def make_call(to_number, message):
    call = twilio_client.calls.create(
        to=to_number,
        from_=twilio_phone_number,
        url="http://demo.twilio.com/docs/voice.xml"  # TwiML URL for a simple message
    )
    print("Calling...")

def process_command(command):
    if "reminder" in command:
        # Extract reminder details using OpenAI
        response = openai.Completion.create(
            engine="davinci",
            prompt="Create a reminder: ",
            max_tokens=50,
            stop=None,
            temperature=0.5
        )
        reminder = response.choices[0].text.strip()
        print("Creating reminder:", reminder)
        return "Reminder set: " + reminder

    elif "to-do list" in command:
        # Extract to-do list item using OpenAI
        response = openai.Completion.create(
            engine="davinci",
            prompt="Add to my to-do list: ",
            max_tokens=30,
            stop=None,
            temperature=0.5
        )
        task = response.choices[0].text.strip()
        print("Adding to-do:", task)
        return "Added to to-do list: " + task

    elif "search" in command:
        # Extract search query using OpenAI
        response = openai.Completion.create(
            engine="davinci",
            prompt="Search the web: ",
            max_tokens=30,
            stop=None,
            temperature=0.5
        )
        query = response.choices[0].text.strip()
        print("Searching the web for:", query)
        return "Search results for: " + query
    elif "send message" in command:
        recipient = input("Enter recipient's phone number: ")
        response = openai.Completion.create(
            engine="davinci",
            prompt="Compose a message: ",
            max_tokens=30,
            stop=None,
            temperature=0.5
        )
        message = response.choices[0].text.strip()
        send_sms(recipient, message)
        return "Message sent: " + message
    elif "send" in command and "message" in command:
        recipient = input("Enter recipient's phone number: ")
        response = openai.Completion.create(
            engine="davinci",
            prompt="Compose a message: ",
            max_tokens=30,
            stop=None,
            temperature=0.5
        )
        message = response.choices[0].text.strip()
        send_sms(recipient, message)
        return "Message sent: " + message
    elif "make" in command and "call" in command:
        recipient = input("Enter recipient's phone number: ")
        response = openai.Completion.create(
            engine="davinci",
            prompt="Compose a call message: ",
            max_tokens=30,
            stop=None,
            temperature=0.5
        )
        message = response.choices[0].text.strip()
        make_call(recipient, message)
        return "Calling with message: " + message
    elif "anime" in command:
        # Change voice to Rem's using VoiceVox
    else:
        return "Sorry, I didn't understand that."

def main():
    speak("Hello! How can I assist you today?")

    while True:
        try:
            text = listen()
            if text:
                response = process_command(text.lower())
                speak(response)
        except KeyboardInterrupt:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()"""
import tkinter as tk
from tkinter import scrolledtext
import pyttsx3
import openai
import requests
from constants import openai_api_key
from constants import twilio_account_sid
from constants import twilio_auth_token
from constants import twilio_phone_number

# Set up the OpenAI API with your API key
openai.api_key = openai_api_key

# Other constants and initialization code

def change_voice_with_voicevox(text):
    # Make a request to the VoiceVoxAPI to change the voice
    voicevox_api_url = "https://your-voicevox-api-endpoint"
    data = {
        "text": text,
        "speaker": "rem"  # Replace with the appropriate VoiceVox speaker name
    }
    response = requests.post(voicevox_api_url, json=data)
    
    if response.status_code == 200:
        return response.text
    else:
        return text  # Return the original text if the voice change fails


def speak_with_voicevox(text):
    rem_voice_text = change_voice_with_voicevox(text)
    engine.say(rem_voice_text)
    engine.runAndWait()

def process_user_input():
    user_input = user_input_text.get("1.0", tk.END).strip()
    if user_input:
        response = process_command(user_input.lower())
        chat_text.insert(tk.END, "\nYou: " + user_input)
        chat_text.insert(tk.END, "\nAssistant: " + response)
        speak_with_voicevox(response)
        user_input_text.delete("1.0", tk.END)

# Other functions
def process_command(command):
    if "reminder" in command:
        # Extract reminder details using OpenAI
        response = openai.Completion.create(
            engine="davinci",
            prompt="Create a reminder: ",
            max_tokens=50,
            stop=None,
            temperature=0.5
        )
        reminder = response.choices[0].text.strip()
        print("Creating reminder:", reminder)
        return "Reminder set: " + reminder

    elif "to-do list" in command:
        # Extract to-do list item using OpenAI
        response = openai.Completion.create(
            engine="davinci",
            prompt="Add to my to-do list: ",
            max_tokens=30,
            stop=None,
            temperature=0.5
        )
        task = response.choices[0].text.strip()
        print("Adding to-do:", task)
        return "Added to to-do list: " + task

    elif "search" in command:
        # Extract search query using OpenAI
        response = openai.Completion.create(
            engine="davinci",
            prompt="Search the web: ",
            max_tokens=30,
            stop=None,
            temperature=0.5
        )
        query = response.choices[0].text.strip()
        print("Searching the web for:", query)
        return "Search results for: " + query
    elif "send message" in command:
        recipient = input("Enter recipient's phone number: ")
        response = openai.Completion.create(
            engine="davinci",
            prompt="Compose a message: ",
            max_tokens=30,
            stop=None,
            temperature=0.5
        )
        message = response.choices[0].text.strip()
        send_sms(recipient, message)
        return "Message sent: " + message
    elif "send" in command and "message" in command:
        recipient = input("Enter recipient's phone number: ")
        response = openai.Completion.create(
            engine="davinci",
            prompt="Compose a message: ",
            max_tokens=30,
            stop=None,
            temperature=0.5
        )
        message = response.choices[0].text.strip()
        send_sms(recipient, message)
        return "Message sent: " + message
    elif "make" in command and "call" in command:
        recipient = input("Enter recipient's phone number: ")
        response = openai.Completion.create(
            engine="davinci",
            prompt="Compose a call message: ",
            max_tokens=30,
            stop=None,
            temperature=0.5
        )
        message = response.choices[0].text.strip()
        make_call(recipient, message)
        return "Calling with message: " + message
    else:
        return "Sorry, I didn't understand that."
"""def main():
    # Initialization code
    
    while True:
        try:
            text = input("User: ")  # Get user input as text
            if text:
                response = process_command(text.lower())
                speak_with_voicevox(response)
        except KeyboardInterrupt:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
"""

engine = pyttsx3.init()

# Create the main application window
app = tk.Tk()
app.title("Rem Chat Assistant")

# Add a picture of Rem
rem_image = tk.PhotoImage(file="./REM.jpg")  # Replace with the actual image file path
rem_label = tk.Label(app, image=rem_image)
rem_label.pack()

# Create a scrolled text widget for the chat
chat_text = scrolledtext.ScrolledText(app, wrap=tk.WORD, height=10, width=40)
chat_text.pack()

# Create a text entry widget for user input
user_input_text = tk.Text(app, wrap=tk.WORD, height=3, width=30)
user_input_text.pack()

# Create a button to process user input
send_button = tk.Button(app, text="Send", command=process_user_input)
send_button.pack()

# Start the GUI event loop
app.mainloop()