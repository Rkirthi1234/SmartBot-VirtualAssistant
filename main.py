from speech_recognition_module import recognize_input
from tts_module import speak
from chatbot_responses import get_response
from wikipedia_module import search_wikipedia
from scheduler_module import schedule_notification_custom_time
from translator_module import translate_text
from trivia_module import start_trivia
from spotify_module import search_and_play

# Main chatbot loop
while True:
    user_input = recognize_input()
    user_input_normalized = user_input.lower()  # Normalize to lowercase

    if user_input_normalized == "exit":
        speak("Goodbye! Have a great day!")
        print("smartbot: Goodbye! Have a great day!")
        break

    if user_input_normalized == "play a game":
        start_trivia()
        continue

    if user_input_normalized == "play a song":
        artist = input("Enter the artist name: ")
        song_name = input("Enter the song name: ")
        search_and_play(f"{artist} {song_name}")
        continue

    response = get_response(user_input_normalized)

    if not response:
        response = search_wikipedia(user_input_normalized)

    if user_input_normalized == "schedule notification":
        receiving_number = input("Enter the receiving number(with country code): ")
        notification_message = input("Enter the notification message: ")
        notification_time = input("Enter the time (HH:MM): ")
        schedule_notification_custom_time(receiving_number, notification_time, notification_message)

    elif user_input_normalized == "translator":
        text_to_translate = input("Enter the sentences: ")
        target_language_code = input("Enter the language code: ")
        translated_text = translate_text(text_to_translate, target_language_code)
        print(f"Translated text: {translated_text}")

        #English - en,Tamil - ta,Hindi - hi,French - fr,Telugu - te,Punjabi - pa,Spanish - es,Arabic - ar,
        #Korean - ko,Marathi - mr,Bengali - bn,Portuguese - pt,Turkish - tr,Chinese(Simplified) - zh-CN,
        #Urdu - ur,Russian - ru,Japanese - ja,German - de,Danish - da,Norwegian - no,Vietnamese - vi,

    speak(response)
    print("smartbot: " + response)
