ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print("Welcome to Caesar Cipher enconde and decode!")
    
while True:
    try:
        choice = int(input("Enter 1 to encode, 2 to decode, or 0 to exit: "))
    except ValueError:
        print("Error: choice must be an integer (0, 1, or 2).")
        continue

    if choice == 0:
        print("Exiting the program. Goodbye!")
        break
    if choice not in (1, 2):
        print("Invalid choice. Please enter 1 to encode, 2 to decode, or 0 to exit.")
        continue

    prase = str(input("Enter the string to encode/decode: "))

    try:
        shift = int(input("Enter the shift value (integer): "))
    except ValueError:
        print("Error: shift value must be an integer.")
        continue

    for ch in prase:
        if ch in ('ç', 'Ç'):
            ch = 'C' if ch.isupper() else 'c'

        upper = ch.upper()
        if upper in ALPHABET:
            if choice == 1:
                index = (ALPHABET.index(upper) + shift) % 26
            else:
                index = (ALPHABET.index(upper) - shift) % 26
            result = ALPHABET[index]

            if ch.islower():
                result = result.lower()
            print(result, end="")
        else:
            print(ch, end="")
    print("\n")