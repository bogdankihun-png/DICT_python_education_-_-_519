formatters = ["plain", "bold", "italic", "header", "link",
              "inline-code", "ordered-list", "unordered-list", "new-line"]
special_commands = ["!help", "!done"]

markdown_text = ""


def print_help():
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
    print("Special commands: !help !done")


while True:
    user_input = input("Choose a formatter: ")

    if user_input == "!help":
        print_help()

    elif user_input == "!done":
        with open("output.md", "w", encoding="utf-8") as file:
            file.write(markdown_text)
        break

    elif user_input not in formatters:
        print("Unknown formatting type or command")

    elif user_input == "plain":
        text = input("Text: ")
        markdown_text += text
        print(markdown_text)

    elif user_input == "bold":
        text = input("Text: ")
        markdown_text += f"**{text}**"
        print(markdown_text)

    elif user_input == "italic":
        text = input("Text: ")
        markdown_text += f"*{text}*"
        print(markdown_text)

    elif user_input == "inline-code":
        text = input("Text: ")
        markdown_text += f"`{text}`"
        print(markdown_text)

    elif user_input == "link":
        label = input("Label: ")
        url = input("URL: ")
        markdown_text += f"[{label}]({url})"
        print(markdown_text)

    elif user_input == "header":
        while True:
            level = int(input("Level: "))
            if 1 <= level <= 6:
                break
            else:
                print("The level should be within the range of 1 to 6")

        text = input("Text: ")
        markdown_text += "#" * level + " " + text + "\n"
        print(markdown_text)

    elif user_input == "new-line":
        markdown_text += "\n"
        print(markdown_text)

    elif user_input in ["ordered-list", "unordered-list"]:
        while True:
            rows = int(input("Number of rows: "))
            if rows > 0:
                break
            else:
                print("The number of rows should be greater than zero")

        for i in range(1, rows + 1):
            row_text = input(f"Row #{i}: ")
            if user_input == "ordered-list":
                markdown_text += f"{i}. {row_text}\n"
            else:
                markdown_text += f"* {row_text}\n"

        print(markdown_text)
