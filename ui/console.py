def show_menu():
    print("==================================================")
    print("Welcome to the PyCipher")
    print("==================================================\n")
    print("Choose the cipher you want to use:")
    print("1. Ceaser Cipher")
    print("2. Affine Cipher")
    print("3. Playfair Cipher")
    print("4. Hill Cipher")
    print("5. Known Plaintext Attack on Hill Cipher")
    print("0. Exit")
    print("==================================================")


def get_choice():
    choice = input("Enter your choice (0-5): ")
    while choice not in ['0', '1', '2', '3', '4', '5']:
        choice = input("Invalid choice. Please enter a number between 0 and 5: ")
    return choice


def get_mode():
    mode = input("Choose Mode (E/D): ").upper()
    while mode not in ['E', 'D']:
        mode = input("Invalid mode. Please enter E for Encryption or D for Decryption: ").upper()
    return mode

def get_text(prompt):
    return input(prompt)


def get_key(prompt):
    return input(prompt)


def show_result(result):
    print("Result:", result)