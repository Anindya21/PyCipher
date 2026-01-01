import numpy as np
import math

'''
Hill Cipher Encryption

key: 2D key matrix 
[17 14
 21 9]

As the key is of 2x2 size, have to process the plaintext 2 letters at a time

plaintext: Random text "Tomorrow is the date to execute the event"--> "TO MO RR OW IS TH ED AT ET OE XE CU TE TH EE VE NT"

ciphertext: Plaintext x key -> C = []
'''
def mod_inverse(a, m=26):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("No modular inverse exists")


def matrix_mod_inverse(key, m=26):
    a, b = key[0]
    c, d = key[1]

    det = (a*d - b*c) % m

    det_inv = mod_inverse(det, m)

    adj = np.array([[ d, -b],
                    [-c,  a]])

    key_inv = (det_inv * adj) % m
    return key_inv


def hill_word_mapper(text,mode, pad=False):
    chars= {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12,
            'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}

    if mode=='w2n':
        mapped_text=[]
        special_chars="0123456789.,?!$%^&*;:}{[]-_`~()@#\\|<>\n\t"

        text= text.translate(str.maketrans('', '', special_chars))
        text = text.replace(" ", "").upper()
        
        if pad and len(text)%2!=0:
            text+="X"

        for ch in text:
            mapped_text.append(chars[ch])

        return mapped_text
    
    elif mode=='n2w':
        reverse_chars = {v: k for k, v in chars.items()}
        return [reverse_chars[n] for n in text]
    
    else:
        raise ValueError("Invalid mode")


def generate_key(key):
    
    key = hill_word_mapper(key, 'w2n', pad=False)
    key = np.array(key).reshape(2,2)

    det = int(np.round(np.linalg.det(key)))

    if math.gcd(det,26) != 1:
        raise ValueError("The key matrix is not invertible. Please provide a valid key.")
    else:
        print(f"Key ---> {key}")
        return key


def generate_ciphertext(plaintext, key):
    
    print_key = key
    key  = generate_key(key)

    ciphertext= []
    
    for i in range(0, len(plaintext), 2):
        
        pair = np.array([[plaintext[i], plaintext[i+1]]])

        print(f"Pair matrix: {pair}")

        cipher_pair = np.matmul(pair, key)%26
        
        # print(f"After multiplication: {cipher_pair}")

        ciphertext.append(cipher_pair[0][0].item())
        ciphertext.append(cipher_pair[0][1].item())


    # print("Ciphertext matrix: ", ciphertext)

    ciphertext = hill_word_mapper(ciphertext, 'n2w', pad=False)
    
    final_cipher= "".join(ciphertext)
    
    plaintext = hill_word_mapper(plaintext, 'n2w', pad=False)
    plaintext= "".join(plaintext)

    with open("hill/bank.txt", "a") as f:
        f.write(f"\nPlaintext: {plaintext} \n Key: {print_key}\n Ciphertext: {final_cipher}\n")

    return final_cipher


def hill_retrieve_plaintext(ciphertext, key):

    key = generate_key(key)

    key_inv = matrix_mod_inverse(key)

    plaintext=[]

    for i in range(0, len(ciphertext), 2):
        
        pair = np.array([[ciphertext[i], ciphertext[i+1]]])

        print(f"Pair matrix: {pair}")

        plain_pair = np.matmul(pair, key_inv)%26
        
        # print(f"After multiplication: {cipher_pair}")

        plaintext.append(int(round(plain_pair[0][0].item())))
        plaintext.append(int(round(plain_pair[0][1].item())))


    # print("Ciphertext matrix: ", ciphertext)

    plaintext = hill_word_mapper(plaintext, 'n2w', pad=False)

    final_plain= "".join(plaintext)

    return final_plain



# print("Hill Cipher Encryption")

# print("----------------------")

# print("For Encryption press E for Decryption press D")

# mode= input("Enter the mode: ")

# if mode.upper() == "E":
#     plaintext= input("Enter the plaintext: ")
#     key = input("Enter the 4 letter key: ")
#     conv_plaintext= hill_word_mapper(plaintext, "w2n",pad=True)
#     cipher = generate_ciphertext(conv_plaintext, key)

# elif mode.upper() == "D":
#     ciphertext= input("Enter the ciphertext: ")
#     key = input("Enter the 4 letter key: ")
#     conv_ciphertext= hill_word_mapper(ciphertext, "w2n", pad=False)
#     plain = hill_retrieve_plaintext(conv_ciphertext, key)

