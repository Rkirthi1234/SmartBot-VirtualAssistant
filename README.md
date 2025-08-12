# SmartBot AI-Powered Virtual Assistant

SmartBot is an advanced AI-powered voice assistant that combines natural language processing, speech recognition, and multiple interactive tools to help users perform everyday tasks hands-free.
From answering questions via Wikipedia, playing trivia games, translating languages, and playing music on Spotify, to scheduling WhatsApp messages — SmartBot is your personal AI companion.

# Features:

- Speech Recognition – Understands and processes your voice commands in real time.

- Text-to-Speech – Delivers natural and clear spoken responses.

- Wikipedia Search – Fetches quick and accurate summaries from Wikipedia.

- Trivia Game – Fun multiple-choice quiz powered by the Open Trivia DB API.

- Spotify Music Playback – Searches and plays your favorite songs directly on Spotify.

- WhatsApp Scheduler – Sends scheduled WhatsApp messages using PyWhatKit.

- Language Translator – Translates sentences into 20+ languages.

- Custom Conversations – Responds to predefined conversational phrases for a personal touch.

# Installation:

- Clone the Repository
  
  git clone https://github.com/your-username/smartbot.git
  
  cd smartbot
  
- Install Dependencies
  
  Ensure Python 3.8+ is installed, then run:
   
  pip install -r requirements.txt
  
- Set Up Spotify API
  
  Create a Spotify Developer account.

  Generate your Client ID and Client Secret.

  Replace them in the code where indicated in smartbot.py and spotify_play.py.

# Usage:

Run the chatbot:

python main.py

# Example Commands:

play a game → Starts the trivia quiz.

play a song → Plays a song by asking for artist and track name.

schedule notification → Schedules a WhatsApp message at a given time.

translator → Translates text into a target language.

Any general question → Searches Wikipedia for the answer.

# Supported Translation Languages:

English (en), Tamil (ta), Hindi (hi), French (fr), Telugu (te), Punjabi (pa), Spanish (es), Arabic (ar), Korean (ko), Marathi (mr), Bengali (bn), Portuguese (pt), Turkish (tr), Chinese Simplified (zh-CN), Urdu (ur), Russian (ru), Japanese (ja), German (de), Danish (da), Norwegian (no), Vietnamese (vi)

# Notes:

- Make sure you are logged in to WhatsApp Web before scheduling messages.

- An active microphone is required for speech recognition.

- Internet connection is needed for Wikipedia, Spotify, translation, and trivia features.

