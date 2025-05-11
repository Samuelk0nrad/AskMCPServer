import sys

if len(sys.argv) < 2:
    print("No filename provided.")
    sys.exit(1)

filename = sys.argv[1].strip('"')
question = sys.argv[2]
predictedAnswer = sys.argv[3]
choices = sys.argv[4].split("\";\"") if len(sys.argv) > 4 else None

GRAY = "\033[90m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

PADDING = 2  # spaces on each side
question_padded = " " * PADDING + question + " " * PADDING
border_len = max(len(question_padded), len(predictedAnswer) + 4)
border = "+" + "-" * border_len + "+"

print()
print(border)
print("|" + BOLD + CYAN + question_padded.ljust(border_len) + RESET + "|")
print(border)
print(GRAY + predictedAnswer + RESET)

if choices:
    print("\nPlease select an option:")
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")
    while True:
        user_input = input("> ")
        if user_input.strip():
            try:
                choice_num = int(user_input)
                if 1 <= choice_num <= len(choices):
                    user_input = choices[choice_num - 1]
                    break
                else:
                    print(f"Please enter a number between 1 and {len(choices)}")
            except ValueError:
                if user_input in choices:
                    break
                print("Please enter a valid option number or exact text")
        else:
            user_input = predictedAnswer
            break
else:
    user_input = input("> ")

with open(filename, "w") as f:
    f.write(user_input if user_input.strip() else predictedAnswer)