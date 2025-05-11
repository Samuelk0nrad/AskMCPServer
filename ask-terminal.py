import sys

if len(sys.argv) < 2:
    print("No filename provided.")
    sys.exit(1)

filename = sys.argv[1].strip('"')
question = sys.argv[2]

user_input = input(f"{question} (Press Enter to finish): ")
with open(filename, "w") as f:
  f.write(user_input)