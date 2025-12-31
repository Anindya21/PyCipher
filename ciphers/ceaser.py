
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
    


def calculate_cipher(plaintext, shift):
    ciphertext= []
    for i in range(0,len(plaintext)):
        cipher_char= (plaintext[i] + shift) % 26
        ciphertext.append(cipher_char)

    ciphertext= word_mapper(ciphertext, 'n2w')    
    
    final_cipher = "".join(ciphertext)
    return final_cipher


def retrieve_plaintext(ciphertext,shift):
    plaintext=[]

    for i in range(0, len(ciphertext)):
        plain_char = (ciphertext[i] - shift) % 26
        plaintext.append(plain_char)
    
    plaintext= word_mapper(plaintext, 'n2w')
    final_plain = "".join(plaintext)
    return final_plain



print("Ceaser Cipher")
print("---------------------")

mode = input("Choose Mode (E/D): ").upper()

if mode == 'E':
    shift= int(input("Enter shift value: "))
    plaintext= input("Enter Plaintext: ")
    ciphertext= calculate_cipher(word_mapper(plaintext,"w2n"), shift)
    print(f"Ciphertext: {ciphertext}", end="")

if mode == 'D':
    shift= int(input("Enter shift value: "))
    ciphertext= input("Enter Ciphertext: ")
    plaintext= retrieve_plaintext(word_mapper(ciphertext,"w2n"), shift)
    print(f"Plaintext: {plaintext}", end="")

