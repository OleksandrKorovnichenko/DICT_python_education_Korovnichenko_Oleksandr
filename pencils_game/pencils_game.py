"""Creation of the game 'Pencils'"""
import random


# function to check if the entered number is integer and positive
def is_positive_integer(value):
    try:
        int_value = int(value)
        return int_value > 0
    except ValueError:
        return False


# function for determining the winning strategy of a bot
def bot_move(pencils):
    if (pencils - 1) % 4 == 0:
        return 3
    elif (pencils - 2) % 4 == 0:
        return 2
    elif (pencils - 3) % 4 == 0:
        return 1
    return random.randint(1, 3)


# user request for the number of pencils (with error handling)
while True:
    print("How many pencils would you like to use:")
    pencils = int(input("> "))
    if is_positive_integer(pencils):
        break
    else:
        print("The number of pencils should be numeric")

# checking that the number of pencils is positive
if pencils == 0:
    print("The number of pencils should be positive")
else:
    # user request for the first player (with error handling)
    while True:
        first_player = input("Who will be the first (John, 🤖 Jack - bot):\n> ")
        if first_player in ["John", "Jack"]:
            break
        else:
            print("Choose between 'John' and '🤖 Jack - bot")

    # check for the names "John" and "Jack" and select the second player
    if first_player == "John":
        second_player = "Jack"
    else:
        second_player = "John"

    # start of the game cycle
    while pencils > 0:

        print("|" * pencils)
        print(first_player + "'s turn:")

        if first_player == "Jack":
            # bot move
            if pencils == 2:
                draw_pencils = random.randint(1, 3)
            elif pencils == 1:
                draw_pencils = 1
            else:
                draw_pencils = bot_move(pencils)
            print(draw_pencils)
        else:
            # player's request for the number of pencils to be removed (with error handling)
            while True:
                try:
                    draw_pencils = int(input("> "))
                    if 1 <= draw_pencils <= 3:
                        if draw_pencils <= pencils:
                            break
                        else:
                            print("Too many pencils were taken")
                    else:
                        print("Possible values: '1', '2' or '3'")
                except ValueError:
                    print("Possible values: '1', '2' or '3'")

        # delete pencils and change the player
        pencils -= draw_pencils
        first_player, second_player = second_player, first_player

    # the game is over, the winner is displayed
    if first_player == "John":
        print("John won!")
    else:
        print("🤖 Jack won!")
