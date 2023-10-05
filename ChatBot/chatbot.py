"""Chat-Bot project: simple types, input-output, strings, calculations, loops"""

bot_name = 'DICTBot`s'
birth_year = 2023

print(f"Hello! My name is {bot_name}.\nI was created in {birth_year}.")
print("Please, remind me your name.")

your_name = input("> ")

print(f"What a great name you have, {your_name}!")
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")

remainder3 = int(input("> "))
remainder5 = int(input("> "))
remainder7 = int(input("> "))

your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

print(f"Your age is {your_age}; that's a good time to start programming!")
print("Now I will prove to you that I can count to any number you want.")

iterations_count = int(input("> "))

for i in range(iterations_count + 1):
    print(f"{i}!")

print("Let's test your programming knowledge.")
print("How can I see the current state of the current branch in Git?")
print("1. git info")
print("2. git status")
print("3. git show status")
print("4. git show")

answer = int(input("> "))

while True:
    if answer < 1 or answer > 4:
        print("There is no such answer. Try from 1 to 4.")
    else:
        if answer == 2:
            print("Completed, have a nice day!")
            break
        else:
            print("Please, try again.")
            answer = int(input("> "))

print("Congratulations, have a nice day!")
