from ciphers.ceaser import (calculate_cipher, retrieve_plaintext)
from ciphers.hill import (hill_word_mapper, generate_ciphertext, hill_retrieve_plaintext)
from ciphers.hill_attack import attack_hill
from ciphers.affine import affine_encrypt, affine_decrypt
from ciphers.playfair import encrypt as playfair_encrypt, decrypt as playfair_decrypt

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

    elif choice == "2":  # Affine Cipher

        if mode == "E":
            text = get_text("Enter the plaintext: ")
            a = int(get_key("Enter key 'a' (coprime with 26): "))
            b = int(get_key("Enter key 'b' (0-25): "))
            result = affine_encrypt(text, a, b, include_non_alpha=True)

        else:
            text = get_text("Enter the ciphertext: ")
            a = int(get_key("Enter key 'a' (coprime with 26): "))
            b = int(get_key("Enter key 'b' (0-25): "))
            result = affine_decrypt(text, a, b, include_non_alpha=True)

        show_result(result)   

    elif choice == "3":  # Playfair Cipher

        if mode == "E":
            text = get_text("Enter the plaintext: ")
            key = get_key("Enter the key: ")
            result, _, _ = playfair_encrypt(text, key)

        else:
            text = get_text("Enter the ciphertext: ")
            key = get_key("Enter the key: ")
            result, _, _ = playfair_decrypt(text, key)

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