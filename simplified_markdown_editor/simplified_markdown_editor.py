"""The user to format the text using the Markdown markup language"""


# Displays information about available formatters and special commands
def help_info():
    print("""Available formatters:
    • plain — звичайний текст без форматування
    • bold/italic — напівжирний/курсив
    • inline-code — вбудований код
    • link — посилання
    • header — Заголовок
    • unordered-list — невпорядкований список
    • ordered-list — упорядкований список
    • new-line — перехід на новий рядок.\n
Special commands: !help !done""")


# Functions for each formatting type
def format_text(formatter):
    return lambda: f"{formatter()}\n"


def plain_text():
    return input("Text: > ")


def bold_text():
    return f"**{input('Text: > ')}**"


def italic_text():
    return f"*{input('Text: > ')}*"


def header_text():
    while True:
        try:
            level = int(input("Level: > "))
            if level < 1 or level > 6:
                print("The level should be within the range of 1 to 6.")
            else:
                return f"{'#' * level} {input('Text: > ')}\n"
        except ValueError:
            print("Please enter a valid integer for the level.")


def link_text():
    label = input("Label: > ")
    url = input("URL: > ")
    return f"[{label}]({url})"


def inline_code_text():
    return f"`{input('Text: > ')}`"


def ordered_list_text():
    formatted_text = "\n"
    while True:
        try:
            num_items = int(input("Number of rows: > "))
            if num_items > 0:
                break
            print("The number of rows should be a positive integer.")
        except ValueError:
            print("Please enter a valid integer for the number of rows.")
    for i in range(num_items):
        formatted_text += f"{i + 1}. {input(f'Row #{i + 1}: > ')}\n"
    return formatted_text


def unordered_list_text():
    formatted_text = "\n"
    while True:
        try:
            num_items = int(input("Number of rows: > "))
            if num_items > 0:
                break
            else:
                print("The number of rows should be a positive integer.")
        except ValueError:
            print("Please enter a valid integer for the number of rows.")
    for _ in range(num_items):
        formatted_text += f"* {input('Text: > ')}\n"
    return formatted_text


def new_line_text():
    return "\n"


# Save text to file
def save_to_file(content):
    with open("output.md", "w") as file:
        file.write(content)


# Main menu of the program
def main_menu():
    formatter_functions = {
        "!help": help_info,
        "plain": format_text(plain_text),
        "bold": format_text(bold_text),
        "italic": format_text(italic_text),
        "header": format_text(header_text),
        "link": format_text(link_text),
        "inline-code": format_text(inline_code_text),
        "ordered-list": ordered_list_text,
        "unordered-list": unordered_list_text,
        "new-line": format_text(new_line_text)
    }

    formatted_elements = []  # List to store all formatted elements
    while True:
        user_input = input("Choose a formatter: > ")
        if user_input == "!done":
            formatted_text = "".join(formatted_elements)  # Concatenate all formatted elements
            save_to_file(formatted_text)
            print("Exiting program...")
            break
        elif user_input == "!help":
            help_info()
        else:
            formatter_function = formatter_functions.get(user_input)
            if formatter_function:
                formatted_elements.append(formatter_function())
                formatted_text = "".join(formatted_elements)
                print(formatted_text)
            else:
                print("Unknown formatting type or command")



if __name__ == "__main__":
    main_menu()
