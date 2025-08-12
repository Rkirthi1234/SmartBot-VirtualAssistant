import speech_recognition as sr
import pywhatkit as pwk
import pyttsx3
import webbrowser 
import wikipedia
import datetime
import sched
import time
import re
import requests
import random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pygetwindow as gw
from googletrans import Translator
from textblob import TextBlob
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='wikipedia')


# Initialize ASR recognizer
recognizer = sr.Recognizer()

# Initialize Text-to-Speech engine with the desired properties
engine = pyttsx3.init()
engine.setProperty('voice', 'your_selected_voice')
engine.setProperty('rate', 150)  # Adjust the speech rate if necessary
engine.setProperty('volume', 1.0)  # Adjust the volume if necessary

# Set up your Spotify API credentials
client_id = "98cefb74f01e44ca9c80a8bf4eb7c0d2"
client_secret = "1579e41852b84a968c363cd08d103b81"

# Authenticate with the Spotify API
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Create a Translator object
translator = Translator()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech input
def recognize_input():
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"User (Speech): {text}")
            return text
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected.")
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results: {e}")
    return input("User (Text): ")  # If no speech input, fallback to text input

# Function to interact with Wikipedia
def search_wikipedia(query):
    wikipedia.set_lang("en")  # Ensure English language search
    try:
        print("Searching Wikipedia for:", query)  # Debugging
        summary = wikipedia.summary(query, sentences=1)  
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return "Multiple results found: " + ", ".join(e.options[:5])  # Show first 5 options
    except wikipedia.exceptions.PageError:
        return "No matching Wikipedia page found."
    except Exception as e:
        return f"An error occurred: {e}"


def display_whatsapp_qr():
    webbrowser.open("https://web.whatsapp.com/")
    print("Please scan the QR code on WhatsApp Web.")
    time.sleep(10)  # Optional: wait for a few seconds before proceeding

    # Minimize the WhatsApp Web window
    time.sleep(15)  # Wait for a bit to ensure the window is open
    try:
        # Get the WhatsApp window and minimize it
        whatsapp_window = gw.getWindowsWithTitle("WhatsApp")[0]  # Adjust the title if necessary
        whatsapp_window.minimize()
        print("WhatsApp Web window minimized.")
    except IndexError:
        print("WhatsApp window not found.")

# Function to schedule a notification at a custom time
def schedule_notification_custom_time(receiving_number, custom_time, notification_message):
    try:
        custom_time = datetime.datetime.strptime(custom_time, "%H:%M")
        now = datetime.datetime.now()
        notification_time = now.replace(hour=custom_time.hour, minute=custom_time.minute, second=0, microsecond=0)

        if now > notification_time:
            notification_time += datetime.timedelta(days=1)  # Schedule for the next day if the time has already passed

        delay = (notification_time - now).total_seconds()
        print(f"Scheduling a notification at {notification_time.strftime('%H:%M')}")

        # Send the message using pywhatkit
        pwk.sendwhatmsg(receiving_number, notification_message, notification_time.hour, notification_time.minute)

    except ValueError:
        print("Invalid time format. Please use HH:MM format.")

def search_and_play(song_name):
    results = sp.search(q=song_name, limit=1, type='track')
    if results['tracks']['items']:
        song_url = results['tracks']['items'][0]['external_urls']['spotify']
        print(f"Found the song! Playing {song_name}...")
        webbrowser.open(song_url)  # Open the song in the default web browser
    else:
        print(f"Sorry, couldn't find the song '{song_name}'.")


# Custom dataset
custom_dataset = {
    "hi!": "Hello! How can I help you?",
    "hello": "Hello! How can I help you?",
    "hello, how are you?": "I'm doing well, thank you. How about you?",
    "what is your name?": "I'm just a smartbot, so I don't have a name. You can call me SB.",
    "good morning!": "Good morning to you too!",
    "good afternoon!": "Good afternoon! How can I assist you today?",
    "good evening!": "Good evening! What can I do for you?",
    "hey!": "Hey there! How can I help you?",
    "how are you?": "I'm just a program, but I'm here to help you!",
    "where are you from?": "I exist in the digital world, so I don't have a physical location.",
    "i love to travel.": "Traveling is great! Where would you like to go?",
    "how can i help you?": "I'm here to provide information and assistance. What can I help you with?",
    "thank you for your help.": "You're welcome! If you have more questions, feel free to ask.",
    "please call me later.": "I'll call you later. Have a great day!",
    "what time is it?": "I don't have access to real-time information, so I can't tell you the current time.",
    "have a nice day!": "You too! Have a wonderful day.",
    "hi!": "Hello! How can I assist you today?",
    "what's up?": "Not much! Just here to help you. What do you need?",
    "greetings!": "Greetings! How can I assist you today?",
    "salutations!": "Salutations! What can I do for you?",
}

# Function to clean and normalize user input
def clean_input(user_input):
    # Convert to lowercase and remove punctuation
    return re.sub(r"[^\w\s]", '', user_input.lower()).strip()

def fetch_trivia():
    url = "https://opentdb.com/api.php?amount=10&type=multiple"  # Fetch 10 multiple choice questions
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        questions = data['results']
        return questions
    else:
        print("Error fetching trivia questions.")
        return []

def start_trivia():
    print("Welcome to the Trivia Quiz!")
    
    questions = fetch_trivia()
    
    if not questions:
        print("Sorry, there was an issue fetching the trivia.")
        return
    
    score = 0
    for i, question_data in enumerate(questions, 1):
        question = question_data['question']
        correct_answer = question_data['correct_answer']
        options = question_data['incorrect_answers']
        options.append(correct_answer)  # Add the correct answer to the options
        random.shuffle(options)  # Shuffle options to randomize their order

        print(f"{i}. Question: {question}")
        print("Options: ")
        for j, option in enumerate(options, 1):  # Use a different variable for options
           print(f"{j}. {option}")
        
        user_answer = input("Your answer (1, 2, 3, or 4): ").strip()
        
        if options[int(user_answer) - 1] == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer was: {correct_answer}")

        print("\n")

    print(f"Your final score: {score}/10")

# Main chatbot loop
while True:
    user_input = recognize_input()
    user_input_normalized = user_input.lower()  # Normalize to lowercase

    if user_input_normalized == "exit":
        speak("Goodbye! Have a great day!")
        print("smartbot: Goodbye! Have a great day!")
        break  # Exit loop

    # Check if the user wants to play trivia before anything else
    if user_input_normalized == "play a game":
        start_trivia()
        continue  # Skip the rest of the loop
        
    if user_input_normalized == "play a song":
        artist = input("Enter the artist name: ")
        song_name = input("Enter the song name: ")
        search_and_play(f"{artist} {song_name}")
        continue  # Skip the rest of the loop after playing the song


    response = ""

    # Check for predefined responses in the custom dataset
    for key in custom_dataset.keys():
        if user_input_normalized == clean_input(key):
            response = custom_dataset[key]
            break  # Exit once a match is found

    # If no response was found, try Wikipedia search
    if not response:
        response = search_wikipedia(user_input_normalized)


    # Handling additional chatbot features
    if user_input_normalized == "schedule notification":
        display_whatsapp_qr()
        receiving_number = input("Please enter the receiving number (with country code): ")
        notification_message = input("Please enter the notification message: ")
        notification_time = input("Please specify the time (HH:MM): ")
        schedule_notification_custom_time(receiving_number, notification_time, notification_message)

    elif user_input_normalized == "translator":
        text_to_translate = input("Enter the sentences: ")
        target_language_code = input("Enter the lang_code: ")
        translated_text = translator.translate(text_to_translate, dest=target_language_code)
        print(f"Translated text in {target_language_code}: {translated_text.text}")
        #English - en,Tamil - ta,Hindi - hi,French - fr,Telugu - te,Punjabi - pa,Spanish - es,Arabic - ar,
        #Korean - ko,Marathi - mr,Bengali - bn,Portuguese - pt,Turkish - tr,Chinese(Simplified) - zh-CN,
        #Urdu - ur,Russian - ru,Japanese - ja,German - de,Danish - da,Norwegian - no,Vietnamese - vi,


    # Speak and print final response
    speak(response)
    print("smartbot: " + response)



        