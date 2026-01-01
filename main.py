print("==================================================")
print("Welcome to the Cipher Suite")
print("Choose the cipher you want to use:")
print("1. Ceaser Cipher")
print("2. Affine Cipher")
print("3. Playfair Cipher")
print("4. Hill Cipher")


choice = input("Enter your choice (1-4): ")


while choice not in ['1','2','3','4']:
    choice = input("Invalid choice. Please enter a number between 1 and 4: ")
    
    if choice == '1':
        