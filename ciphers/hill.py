import numpy as np
import random
import math


'''
Playfair Cipher Encryption

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

def convert_plaintext(plaintext):
    
    word = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, 
            "L":11, "M":12, "N":13, "O":14, "P":15, "Q":16, "R":17, "S":18, "T":19, "U":20, 
            "V":21, "W":22, "X":23, "Y":24,"Z":25}
    
    special_chars=".,?!$%^&*;:}{[]-_`~()@#\\|<>\n\t"

    plaintext= plaintext.translate(str.maketrans('', '', special_chars))
    plaintext = plaintext.replace(" ", "")

    plaintext= plaintext.upper()

    conv_plaintext= []
    if len(plaintext)%2!=0:
        plaintext+= "X"

    for i in range(0, len(plaintext), 1):
        conv_plaintext.append(plaintext[i:i+1])
    

    for i in range(0,len(conv_plaintext)):
        conv_plaintext[i] = word[conv_plaintext[i]]
         
    return conv_plaintext

def convert_ciphertext(ciphertext):

    word = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, 
            "L":11, "M":12, "N":13, "O":14, "P":15, "Q":16, "R":17, "S":18, "T":19, "U":20, 
            "V":21, "W":22, "X":23, "Y":24,"Z":25}    
    
    conv_ciphertext= []
    
    for i in range(0, len(ciphertext), 1):
        conv_ciphertext.append(ciphertext[i:i+1])
    

    for i in range(0,len(conv_ciphertext)):
        conv_ciphertext[i] = word[conv_ciphertext[i]]
         
    return conv_ciphertext


def word_mapper(text):
    word = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, 
            "L":11, "M":12, "N":13, "O":14, "P":15, "Q":16, "R":17, "S":18, "T":19, "U":20, 
            "V":21, "W":22, "X":23, "Y":24,"Z":25}
    text= text.upper()

    mapped_text= []
    for i in range(0,len(text)):
        if text[i] in word:
            mapped_text.append(word[text[i]])
    
    return mapped_text


def generate_key(key):
    #key = np.random.randint(0,26,size=(2,2))
    key = word_mapper(key)
    key = np.array(key).reshape(2,2)

    det = int(np.round(np.linalg.det(key)))

    if math.gcd(det,26) != 1:
        raise ValueError("The key matrix is not invertible. Please provide a valid key.")
    else:
        print(f"Key ---> {key}")
        return key



def generate_ciphertext(plaintext, key):
    
    word = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, 
            "L":11, "M":12, "N":13, "O":14, "P":15, "Q":16, "R":17, "S":18, "T":19, "U":20, 
            "V":21, "W":22, "X":23, "Y":24,"Z":25}
    
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

    for i in range(0,len(ciphertext)):
        if ciphertext[i] in word.values():

            for key, value in word.items():
                if value == ciphertext[i]:
                    ciphertext[i] = key

    
    final_cipher= "".join(ciphertext)
    
    with open("../hill/bank.txt", "a") as f:
        f.write(f"\nPlaintext: {plaintext} \n Key: {print_key}\n Ciphertext: {final_cipher}\n")

    return print(f"Ciphertext- {final_cipher}")


def retrieve_plaintext(ciphertext, key):

    word = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, 
            "L":11, "M":12, "N":13, "O":14, "P":15, "Q":16, "R":17, "S":18, "T":19, "U":20, 
            "V":21, "W":22, "X":23, "Y":24,"Z":25}    

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

    for i in range(0,len(plaintext)):
        for key, value in word.items():
            if value == plaintext[i]:
                plaintext[i] = key
                break

    
    final_plain= "".join(plaintext)

    return print(f"Plaintext- {final_plain}")







# class HillCipher():

#     def __init__(self, plaintext, key):
#         self.plaintext = plaintext
#         self.key = key
        

#     def generate_key(self):
#         if self.key is None:
#             self.key = np.random.randint(0,26,size=(2,2))
#             print(f"Key ---> {self.key}")
        
#         return self.key

#     def convert_plaintext(self):
#         word = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, 
#                 "L":11, "M":12, "N":13, "O":14, "P":15, "Q":16, "R":17, "S":18, "T":19, "U":20, 
#                 "V":21, "W":22, "X":23, "Y":24,"Z":25}
        
#         special_chars=".,?!$%^&*;:}{[]-_`~()@#\'/\\|<>\n\t"

#         plaintext= self.plaintext.translate(str.maketrans('', '', special_chars))
#         self.plaintext= self.plaintext.upper()

#         conv_plaintext= []
#         if len(self.plaintext)%2!=0:
#             self.plaintext+= "X"

#         for i in range(0, len(self.plaintext), 1):
#             conv_plaintext.append(self.plaintext[i:i+1])
        

#         for i in range(0,len(conv_plaintext)):
#             if conv_plaintext[i] in word:
#                 conv_plaintext[i] = word[conv_plaintext[i]]
             
#         return conv_plaintext



print("Hill Cipher Encryption")

print("----------------------")

print("For Encryption press E for Decryption press D")

mode= input("Enter the mode: ")

if mode.upper() == "E":
    plaintext= input("Enter the plaintext: ")
    key = input("Enter the 4 letter key: ")
    conv_plaintext= convert_plaintext(plaintext)
    cipher = generate_ciphertext(conv_plaintext, key)

elif mode.upper() == "D":
    ciphertext= input("Enter the ciphertext: ")
    key = input("Enter the 4 letter key: ")
    conv_ciphertext= convert_ciphertext(ciphertext)
    plain = retrieve_plaintext(conv_ciphertext, key)
# ciphertext= input("Enter the ciphertext: ")
# conv_ciphertext= convert_ciphertext(ciphertext)

# print(conv_ciphertext)