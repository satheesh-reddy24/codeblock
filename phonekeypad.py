def phone_keypad(number):
    # Define the mapping from numbers to letters
    keypad = {
        '0': ' ',
        '1': '',
        '2': 'ABC',
        '3': 'DEF',
        '4': 'GHI',
        '5': 'JKL',
        '6': 'MNO',
        '7': 'PQRS',
        '8': 'TUV',
        '9': 'WXYZ'
    }
    
    # Convert the input number to uppercase to handle lowercase letters
    number = number.upper()
    
    # Initialize an empty string to store the result
    result = ''
    
    # Iterate over each character in the input string
    for char in number:
        # Check if the character is a digit
        if char.isdigit():
            # Append the corresponding letters to the result
            result += keypad[char]
        else:
            # If the character is not a digit, append it as is
            result += char
    
    return result

# Example usage
if __name__ == "__main__":
    phone_number = input("Enter a phone number or text: ")
    keypad_sequence = phone_keypad(phone_number)
    print("Keypad sequence:", keypad_sequence)