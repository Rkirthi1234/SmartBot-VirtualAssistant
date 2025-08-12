from speech_recog import recognize_input
from text_to_speech import speak
from wikipedia_search import search_wikipedia
from whatsapp_schedule import display_whatsapp_qr, schedule_notification_custom_time
from spotify_play import search_and_play
from translator_module import translate_text
from trivia_game import start_trivia
from responses import custom_dataset, clean_input

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
    
    
    # Handling additional chatbot features
    if user_input_normalized == "schedule notification":
        display_whatsapp_qr()
        receiving_number = input("Please enter the receiving number (with country code): ")
        notification_message = input("Please enter the notification message: ")
        notification_time = input("Please specify the time (HH:MM): ")
        schedule_notification_custom_time(receiving_number, notification_time, notification_message)
        continue

    if user_input_normalized == "translator":
        translate_text()
        continue

        #English - en,Tamil - ta,Hindi - hi,French - fr,Telugu - te,Punjabi - pa,Spanish - es,Arabic - ar,
        #Korean - ko,Marathi - mr,Bengali - bn,Portuguese - pt,Turkish - tr,Chinese(Simplified) - zh-CN,
        #Urdu - ur,Russian - ru,Japanese - ja,German - de,Danish - da,Norwegian - no,Vietnamese - vi,

    response = ""

    # Check for predefined responses in the custom dataset
    for key in custom_dataset.keys():
        if user_input_normalized == clean_input(key):
            response = custom_dataset[key]
            break  # Exit once a match is found

    # If no response was found, try Wikipedia search
    if not response:
        response = search_wikipedia(user_input_normalized)
    
    
    # Speak and print final response
    speak(response)
    print("smartbot: " + response)



        