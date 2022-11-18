PLACEHOLDER = "[name]"


with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        striped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, striped_name)
        with open(f"Output/ReadyToSend/letter_for_{striped_name}.txt", "w") as new_file:
            new_file.write(new_letter)