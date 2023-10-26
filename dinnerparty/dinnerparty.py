"""Programs for sharing common costs"""
import random

# friends list
friends = {}


# the function of adding friends to the list
def adding_friends(count):
    print('Enter the name of every friend (including you), each on a new line:')
    for i in range(count):
        friend_name = input('> ')
        friends[friend_name] = 0
    return friends


# account distribution function
def split_bill(count):
    print('Enter the total amount:')
    total_amount = int(input('> '))
    amount_per_friend = round(total_amount / count, 2)  # divide the bill equally among all your friends.

    for friend_name in friends:
        friends[friend_name] = amount_per_friend
    return total_amount, friends


# the logic of removing the lucky ticket
def lucky_ticket(total_amount, count):
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky_input = input('> ')

    # if the user decided to choose "lucky" (Yes), select a name from the dictionary at random.
    if lucky_input.lower() == "yes":
        lucky_friend = random.choice(list(friends.keys()))
        print(f"{lucky_friend} is the lucky one!")

        friends[lucky_friend] = 0
        amount_per_friend = round(total_amount / (count - 1), 2)
        for friend_name in friends:
            if friends[friend_name] != 0:
                friends[friend_name] = amount_per_friend
        return friends
    elif lucky_input.lower() == "no":
        print("No one is going to be lucky")
    else:
        print("Write Yes/No!")
        print("No one is going to be lucky")


print('Enter the number of friends joining (including you):')

count = int(input('> '))  # number of friends
if count <= 0:
    print('No one is joining for the party')
else:
    adding_friends(count=count)
    total_amount, friends = split_bill(count=count)
    lucky_ticket(total_amount, count)
    print(friends)
