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
    "what's up?": "Not much! Just here to help you. What do you need?",
    "greetings!": "Greetings! How can I assist you today?",
    "salutations!": "Salutations! What can I do for you?",
}

import re
def clean_input(user_input):
    return re.sub(r"[^\w\s]", '', user_input.lower()).strip()

