
# Template for the letter
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
name = input("Enter the name: ")
date = input("Enter the date (e.g., 17-05-2025): ")

# Replacing the placeholders with actual values
letter_filled = letter.replace("<|Name|>", name)
letter_filled = letter_filled.replace("<|Date|>", date)

# Printing the final letter
print("\nFinal Letter:")
print(letter_filled)