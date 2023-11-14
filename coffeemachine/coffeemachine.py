"""Creating a coffee machine simulator"""


# class definition for a CoffeeMachine
class CoffeeMachine:
    # constructor initializes the machine's state and supplies
    def __init__(self):
        # initial supplies of ingredients
        self.ingredients = {"water": 400, "milk": 540, "coffee_beans": 120, "disposable_cups": 9}
        # current amount of money in the machine
        self.money = 550
        # prices for different coffee options
        self.prices = {"1": 4, "2": 7, "3": 6}
        # current state of the machine, starts with the main menu
        self.state = "main_menu"

    # method to process user input and take appropriate actions
    def process_input(self, user_input):
        # check user input and execute corresponding action
        if user_input == "buy":
            self.state = "buy"
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:")
            user_input = input("> ")
            self.process_buy(user_input)
        elif user_input == "fill":
            self.state = "fill"
            print("Write how many ml of water you want to add:")
            user_input = input("> ")
            self.fill_supplies(user_input)
        elif user_input == "take":
            self.take_money()
        elif user_input == "remaining":
            self.display_status()
        elif user_input == "exit":
            return
        else:
            print("Invalid action. Please choose buy, fill, take, remaining, or exit.")

    # method to process the "buy" action and make the selected coffee
    def process_buy(self, user_input):
        if user_input == "back":
            self.state = "main_menu"
        elif user_input in self.prices:
            if self.can_make_coffee(user_input):
                print("I have enough resources, making you a coffee!")
                self.make_coffee(user_input)
            else:
                print("Sorry, not enough resources to make coffee!")
            self.state = "main_menu"
        else:
            print("Invalid choice. Please choose 1, 2, 3, or back.")

    # method to check if there are enough supplies to make the selected coffee
    def can_make_coffee(self, choice):
        required_water = 200 if choice != "2" else 350
        required_milk = 50 if choice == "3" else 0 if choice == "1" else 75
        required_coffee_beans = 15 if choice != "3" else 12
        required_disposable_cups = 1

        return (
                self.ingredients["water"] >= required_water
                and self.ingredients["milk"] >= required_milk
                and self.ingredients["coffee_beans"] >= required_coffee_beans
                and self.ingredients["disposable_cups"] >= required_disposable_cups
        )

    # method to update supplies and money after making a coffee
    def make_coffee(self, choice):
        self.ingredients["water"] -= 200 if choice != "2" else 350
        self.ingredients["milk"] -= 50 if choice == "3" else 0 if choice == "1" else 75
        self.ingredients["coffee_beans"] -= 15 if choice != "3" else 12
        self.ingredients["disposable_cups"] -= 1
        self.money += self.prices[choice]

    # method to fill the supplies based on user input
    def fill_supplies(self, user_input):
        if user_input.isdigit():
            self.ingredients["water"] += int(user_input)
            print("Write how many ml of milk you want to add:")
            self.ingredients["milk"] += int(input())
            print("Write how many grams of coffee beans you want to add:")
            self.ingredients["coffee_beans"] += int(input())
            print("Write how many disposable coffee cups you want to add:")
            self.ingredients["disposable_cups"] += int(input())
        else:
            print("Invalid input. Please enter a number.")

    # method to withdraw money and display the amount withdrawn
    def take_money(self):
        print(f"I gave you {self.money}")
        self.money = 0

    # method to display the current status of the coffee machine
    def display_status(self):
        print(f"The coffee machine has:")
        print(f"{self.ingredients['water']} of water")
        print(f"{self.ingredients['milk']} of milk")
        print(f"{self.ingredients['coffee_beans']} of coffee beans")
        print(f"{self.ingredients['disposable_cups']} of disposable cups")
        print(f"{self.money} of money")


# main menu function to interact with the CoffeeMachine
def main_menu():
    # create a CoffeeMachine instance
    coffee_machine = CoffeeMachine()

    # loop to keep the program running until the user chooses to exit
    while True:
        print("Write action (buy, fill, take, remaining, exit):")
        action = input("> ")
        coffee_machine.process_input(action)
        if action == "exit":
            break


# execute the main_menu function if the script is run directly
if __name__ == "__main__":
    main_menu()
