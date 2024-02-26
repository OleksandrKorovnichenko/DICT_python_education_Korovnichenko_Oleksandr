"""Arithmetic tests"""
import random


# generating mathematical examples
def generate_arithmetic(level):
    if level == 1:
        num1 = random.randrange(2, 9)
        num2 = random.randrange(2, 9)
        operation = random.choice(['+', '-', '*'])
        arithmetic = f"{num1} {operation} {num2}"
        return arithmetic, eval(arithmetic)
    elif level == 2:
        num = random.randrange(11, 29)
        return num, (num ** 2)
    else:
        raise ValueError("Invalid level")


# saving the result to a file
def save_result_to_file(name, score, level, level_description):
    with open("results.txt", "a") as file:
        file.write(f"{name}: {score}/5 in level {level} ({level_description}).\n")


# main logic and user input processing
def main():
    print("Choose difficulty level:")
    print("1. Simple arithmetic operations with numbers from 2 to 9.")
    print("2. Squaring numbers from 11 to 29.")

    while True:
        try:
            level = int(input("Enter your choice (1 or 2): "))
            if level not in [1, 2]:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")

    questions_count = 5
    correct_answers = 0
    prev_question = None

    for i in range(questions_count):
        while True:
            if prev_question:
                question, answer = prev_question
            else:
                question, answer = generate_arithmetic(level)
            user_input = input(f"{question}\n> ")
            try:
                user_answer = int(user_input)
                if user_answer == answer:
                    print("Right!")
                    correct_answers += 1
                    prev_question = None
                else:
                    print("Wrong!")
                    prev_question = None
                break
            except ValueError:
                print("Incorrect format.")
                prev_question = (question, answer)

    print(f"Your mark is {correct_answers}/{questions_count}.")

    # processing save results
    save_result = input("Would you like to save your result to the file? Enter yes or no: ")
    if save_result.lower() in ['yes', 'y']:
        name = input("Enter your name: ")
        level_description = "Simple arithmetic operations with numbers from 2 to 9." \
            if level == 1 else "Squaring numbers from 11 to 29."
        save_result_to_file(name, correct_answers, level, level_description)
        print("Result has been saved to results.txt.")


if __name__ == "__main__":
    main()
