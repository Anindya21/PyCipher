import numpy as np
import math

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

def word_mapper(text,mode):
    chars= {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12,
            'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}

    if mode=='w2n':
        mapped_text=[]
        special_chars=".,?!$%^&*;:}{[]-_`~()@#\\|<>\n\t"

        text= text.translate(str.maketrans('', '', special_chars))
        text = text.replace(" ", "").upper()
        
        for ch in text:
            mapped_text.append(chars[ch])

        return mapped_text
    
    elif mode=='n2w':
        reverse_chars = {v: k for k, v in chars.items()}
        return [reverse_chars[n] for n in text]


def attack_hill(known_plaintext, known_ciphertext):
    
    known_plaintext= word_mapper(known_plaintext, 'w2n')
    known_ciphertext= word_mapper(known_ciphertext, 'w2n')

    
    if len(known_plaintext) < 4 or len(known_ciphertext) < 4:
        raise ValueError("At least 4 characters of known plaintext and ciphertext are required.")


    plain_matrix = np.array([
        [known_plaintext[0], known_plaintext[1]],
        [known_plaintext[2], known_plaintext[3]]
    ])

    cipher_matrix= np.array([
        [known_ciphertext[0], known_ciphertext[1]],
        [known_ciphertext[2], known_ciphertext[3]]
    ])

    det = int(np.round(np.linalg.det(plain_matrix))) % 26

    if math.gcd(det, 26) != 1:
        raise ValueError("The known plaintext matrix is not invertible modulo 26.")

    P_inv = matrix_mod_inverse(plain_matrix, 26)

    key = np.matmul(P_inv, cipher_matrix) % 26

    return key


kp = input("Enter known plaintext (min 4 letters): ")
kc = input("Enter corresponding ciphertext: ")

recovered_key = attack_hill(kp, kc)

recovered_key_letters = word_mapper(recovered_key.flatten().tolist(), 'n2w')

recovered_key_letters = "".join(recovered_key_letters)
print(f"Key --> {recovered_key_letters}")