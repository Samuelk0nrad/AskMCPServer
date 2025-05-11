import sys

if len(sys.argv) < 2:
    print("No filename provided.")
    sys.exit(1)

filename = sys.argv[1].strip('"')
question = sys.argv[2]

GRAY = "\033[90m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

PADDING = 2  # spaces on each side
question_padded = " " * PADDING + question + " " * PADDING
border_len = len(question_padded)
border = "+" + "-" * border_len + "+"

print()
print(border)
print("|" + BOLD + CYAN + question_padded + RESET + "|")
print(border)

user_input = input("> ")
with open(filename, "w") as f:
  f.write(user_input)
