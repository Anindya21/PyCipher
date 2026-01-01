from ciphers.ceaser import (calculate_cipher, retrieve_plaintext)
from ciphers.hill import (hill_word_mapper, generate_ciphertext, hill_retrieve_plaintext)
from ciphers.hill_attack import attack_hill

from ui.console import (
    show_menu,
    get_choice,
    get_mode,
    get_text,
    get_key,
    show_result
)

def main():
    show_menu()
    choice = get_choice()
    
    if choice in {"1", "2", "3", "4"}:
        mode = get_mode()

    if choice=="0":
        print("Exiting program.")
        return

    if choice == "1":
        
        if mode== "E":
            text= get_text("Enter the plaintext: ")
            shift= int(get_text("Enter Shift (Default 3): "))
            result= calculate_cipher(text, shift)

        else:
            text= get_text("Enter the ciphertext: ")
            shift= int(get_text("Enter Shift (Default 3): "))
            result= retrieve_plaintext(text, shift)
    
        show_result(result)

    elif choice == "4":

        if mode=="E":
            text = get_text("Enter the plaintext: ")
            key = get_key("Enter the 4 letter key: ")

            conv_text= hill_word_mapper(text,"w2n", pad=True)
            result= generate_ciphertext(conv_text,key)

        else:
            text = get_text("Enter the ciphertext: ")
            key = get_key("Enter the 4 letter key: ")
            conv_text= hill_word_mapper(text, "w2n", pad=False)

            result = hill_retrieve_plaintext(conv_text,key)

        show_result(result)
    
    elif choice == "5":

        plain= get_text("Enter Known Plaintext: ")
        cipher= get_text("Enter Known Ciphertext: ")
        
        result= attack_hill(plain,cipher)

        show_result(result)


if __name__ == "__main__":
    main()