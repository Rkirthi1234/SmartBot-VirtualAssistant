import requests
import random

def fetch_trivia():
    url = "https://opentdb.com/api.php?amount=10&type=multiple"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data['results']
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
        options = question_data['incorrect_answers'] + [correct_answer]
        random.shuffle(options)

        print(f"{i}. {question}")
        for j, option in enumerate(options, 1):
            print(f"{j}. {option}")

        user_answer = input("Your answer (1, 2, 3, or 4): ").strip()

        if options[int(user_answer) - 1] == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer was: {correct_answer}")

        print("\n")

    print(f"Your final score: {score}/10")
