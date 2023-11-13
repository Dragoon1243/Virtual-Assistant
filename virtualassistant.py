import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import random

# Initialize the speech recognition engine
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the voice for assistant
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Function to greet the user based on time of the day
def greey():
    current_time = datetime.datetime.now().hour
    if current_time < 12:
        engine.say("Good morning, sir. How can I help you?")
    elif 12 <= current_time < 18:
        engine.say("Good afternoon, sir. How can I assist you?")
    else:
        engine.say("Good evening, sir. How may I assist you?")
    engine.runAndWait()

# Function to open any application
def open_application(application_name):
    if "chrome" in application_name:
        engine.say("Opening Google Chrome")
        webbrowser.open("chrome")
    elif "notepad" in application_name:
        engine.say("Opening Notepad")
        os.startfile("notepad.exe")
    elif "spotify" in application_name:
        engine.say("Opening Spotify")
        os.startfile("spotify.exe")
    else:
        engine.say("Application not found")

# Function to play vedio songs from youtube
def play_video_song(song_name):
    engine.say(f"Playing (song_name) video on youtube")
    webbrowser.open(f"https://www.youtube.com/results?search_query={song_name}")

# Function to play audio songs from spotify
def play_audio_song(song_name):
    engine.say(f"Playing (song_name) audio on Spotify")
    webbrowser.open(f"https://www.spotify.com/results?search_query={song_name}")

def get_time_and_date():
    current_time = datetime.datetime.now().strftime("%H:%M")
    current_date = datetime.datetime.now().strftime("%d-%m-%Y")
    engine.say(f"The current time is {current_time} and the date is {current_date}")

# Function to exit program
def exit_assistant():
    engine.say("Goodbye, sir. Have a great day!")
    engine.runAndWait()
    exit()

# Main program loop
while True:
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio)
        print(f"User: {query}")
        if "open" in query:
            application_name = query.split("open ")[1]
            open_application(application_name)
        elif "play" in query:
            if "video" in query:
                song_name = query.split("play ")[1].split(" video")[0]
                play_video_song(song_name)
            elif "audio" in query:
                song_name = query.split("play ")[1].split(" audio")[0]
                play_audio_song(song_name)
        elif "time" in query and "date" in query:
            get_time_and_date()
        elif "exit" in query:
            exit_assistant()
        else:
            engine.say("Sorry, I didn't understand. can you please repeat?")
    except sr.UnknownValueError:
        engine.say("Sorry, I didn't catch that, Can you please repeat?")
    except sr.RequestError:
        engine.say("Sorry, I'm having trouble connecting to the internet. Please try again later.")

    engine.runAndWait()
