"""Rock, paper, scissors game"""
import random


# Function for reading ratings from a file
def read_ratings():
    rating = {}
    try:
        with open("rating.txt", "r") as file:
            for line in file:
                names, score = line.split()
                rating[names] = int(score)
    except FileNotFoundError:
        pass
    return rating


# A function for updating ratings and writing them to a file
def update_ratings(rang, nick, score):
    rang[nick] = score
    with open("rating.txt", "w") as file:
        for nick, score in rang.items():
            file.write(nick + " " + str(score) + "\n")


# A function for defining relationships between elements
def determine_relationship(options):
    relationship = {}
    half = len(options) // 2
    for i, option in enumerate(options):
        winners = options[i - half:i] + options[i + 1 + half:]
        losers = options[i + 1:i + 1 + half] + options[:i - half]
        relationship[option] = {'win': winners, 'lose': losers}
    return relationship


# A function that selects a random variantт
def computer_choice(options):
    return random.choice(options)


# Function to determine the winner
def determine_winner(user_choice, computer_picks, relations):
    if user_choice == computer_picks:
        return "Draw", computer_picks
    elif computer_picks in relations[user_choice]['win']:
        return "Win", computer_picks
    else:
        return "Lose", computer_picks


# Getting the name from the user
name = input("Enter your name:> ")
print("Hello,", name)

# Reading ratings
ratings = read_ratings()
user_score = ratings.get(name, 0)

# Getting game options from the user
user_options_input = input(
    "Enter options separated by comma (or leave empty for default 'rock,paper,scissors'):> ").strip()
if user_options_input:
    user_options = user_options_input.split(',')
else:
    user_options = ['rock', 'paper', 'scissors']

print("Okay, let's start.")

# Determination of relations between game variants
relationships = determine_relationship(user_options)

# The main cycle of the game
while True:
    user_input = input("Enter your choice, or type !rating or !exit to quit:> ").lower()

    if user_input == "!exit":
        print("Bye!")
        break
    elif user_input == "!rating":
        print("Your rating:", user_score)
        continue
    elif user_input not in user_options:
        print("Invalid input.")
        continue

    # Selection of a random option by the computer and determination of the winner
    computer_pick = computer_choice(user_options)
    result, computer_pick = determine_winner(user_input, computer_pick, relationships)

    # Updating the user's rating and outputting the result
    if result == "Draw":
        user_score += 50
        print("There is a draw (" + computer_pick + ")")
    elif result == "Win":
        user_score += 100
        print("Well done. The computer chose", computer_pick, "and failed")
    else:
        print("Sorry, but the computer chose", computer_pick)

    update_ratings(ratings, name, user_score)
