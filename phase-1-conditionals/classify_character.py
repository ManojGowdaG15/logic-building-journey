# Check whether a character is a vowel, consonant, digit, or symbol

char = input("Enter a single character: ")

if len(char) != 1:
    print("Error: Please enter exactly one character.")
else:
    # 1. First, check if it's an alphabetical letter
    if char.isalpha():
        if char.lower() in 'aeiou':
            print(f"The character '{char}' is a vowel.")
        else:
            print(f"The character '{char}' is a consonant.")
            
    # 2. Next, check if it's a numeric digit
    elif char.isdigit():
        print(f"The character '{char}' is a digit.")
        
    # 3. If it's neither a letter nor a digit, it's a symbol
    else:
        print(f"The character '{char}' is a symbol.")
