def letter_to_code(word):
    # Create the mapping based on the provided codes
    mapping = {
        'C': '1', 'A': '2', 'M': '3', 'P': '4', 'H': '5', 'O': '6', 'R': '7',
        'W': '8', 'I': '9', 'E': '0'
    }
    
    # Generate the code for the input word
    code = ''.join(mapping[letter] for letter in word)
    return code

# Input word
word = "WARRIOR"
# Get the code
code = letter_to_code(word)
print(f"The code for '{word}' is: {code}")
