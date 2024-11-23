# quiz.py
from questions import get_questions
from utils import display_question, calculate_score, get_result

def start_quiz():
    print("Welcome to the CLI Quiz App!")
    print("Answer the questions by typing the correct option (e.g., A, B, C, or D).\n")

    questions = get_questions()
    total_questions = len(questions)
    correct_answers = 0

    for index, q in enumerate(questions, start=1):
        print(f"Question {index}/{total_questions}")
        display_question(q["question"], q["options"])
        user_answer = input("Your answer: ").strip().upper()

        if user_answer == q["answer"]:
            print("Correct! 🎉")
            correct_answers += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")
    
    score = calculate_score(correct_answers, total_questions)
    result = get_result(score)

    print(f"\nQuiz Completed! Your Score: {score:.2f}%")
    print(f"You {result} the quiz.")

if __name__ == "__main__":
    start_quiz()
