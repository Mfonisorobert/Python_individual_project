# utils.py
def display_question(question, options):
    print("\n" + question)
    for option in options:
        print(option)

def calculate_score(correct_answers, total_questions):
    return (correct_answers / total_questions) * 100

def get_result(score, pass_mark=50):
    return "PASS" if score >= pass_mark else "FAIL"
