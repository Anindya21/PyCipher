"""
AFFINE CIPHER IMPLEMENTATION
=============================
The Affine Cipher is a type of monoalphabetic substitution cipher.
Encryption formula: E(x) = (a*x + b) mod 26
Decryption formula: D(x) = a^(-1)*(x - b) mod 26
where:
- x is the letter's position (0-25)
- a must be coprime with 26 (gcd(a, 26) = 1)
- b is any integer (0-25)
- a^(-1) is the modular multiplicative inverse of a mod 26
"""

def gcd(a, b):
    """
    Calculate Greatest Common Divisor using Euclidean algorithm.
    Needed to check if 'a' is coprime with 26.
    """
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m=26):
    """
    Find modular multiplicative inverse of a mod m.
    Returns x such that (a*x) % m = 1
    This is needed for decryption.
    """
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None  # No inverse exists

def validate_key(a, b):
    """
    Validate that 'a' is valid for Affine Cipher.
    'a' must be coprime with 26 (gcd(a, 26) = 1).
    """
    if gcd(a, 26) != 1:
        raise ValueError(f"Key 'a'={a} is not valid. 'a' must be coprime with 26.")
    if not (0 <= b < 26):
        raise ValueError(f"Key 'b'={b} is not valid. 'b' must be between 0 and 25.")
    return True

def affine_encrypt(text, a, b, include_non_alpha=False):
    """
    Encrypt text using Affine Cipher.
    
    Parameters:
    - text: String to encrypt
    - a: First key (must be coprime with 26)
    - b: Second key (0-25)
    - include_non_alpha: If True, keep non-alphabet characters as-is
    
    Returns: Encrypted string
    """
    # Validate the key first
    validate_key(a, b)
    
    encrypted_text = []
    
    for char in text:
        if char.isalpha():
            # Convert to uppercase for consistency
            char_upper = char.upper()
            
            # Get character's position (A=0, B=1, ..., Z=25)
            x = ord(char_upper) - ord('A')
            
            # Apply Affine Cipher encryption formula: E(x) = (a*x + b) mod 26
            encrypted_x = (a * x + b) % 26
            
            # Convert back to character
            encrypted_char = chr(encrypted_x + ord('A'))
            
            # Preserve original case
            if char.islower():
                encrypted_char = encrypted_char.lower()
            
            encrypted_text.append(encrypted_char)
        else:
            # Handle non-alphabetic characters
            if include_non_alpha:
                encrypted_text.append(char)
            else:
                # Skip or handle as needed
                encrypted_text.append('')
    
    return ''.join(encrypted_text)

def affine_decrypt(cipher_text, a, b, include_non_alpha=False):
    """
    Decrypt text using Affine Cipher.
    
    Parameters:
    - cipher_text: String to decrypt
    - a: First key (must be coprime with 26)
    - b: Second key (0-25)
    - include_non_alpha: If True, keep non-alphabet characters as-is
    
    Returns: Decrypted string
    """
    # Validate the key first
    validate_key(a, b)
    
    # Find modular inverse of 'a' mod 26
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError(f"No modular inverse exists for a={a} mod 26")
    
    decrypted_text = []
    
    for char in cipher_text:
        if char.isalpha():
            # Convert to uppercase for consistency
            char_upper = char.upper()
            
            # Get character's position (A=0, B=1, ..., Z=25)
            y = ord(char_upper) - ord('A')
            
            # Apply Affine Cipher decryption formula: D(y) = a^(-1)*(y - b) mod 26
            # Note: In Python, (y - b) % 26 handles negative numbers correctly
            decrypted_x = (a_inv * (y - b)) % 26
            
            # Convert back to character
            decrypted_char = chr(decrypted_x + ord('A'))
            
            # Preserve original case
            if char.islower():
                decrypted_char = decrypted_char.lower()
            
            decrypted_text.append(decrypted_char)
        else:
            # Handle non-alphabetic characters
            if include_non_alpha:
                decrypted_text.append(char)
            else:
                # Skip or handle as needed
                decrypted_text.append('')
    
    return ''.join(decrypted_text)

def get_valid_a_values():
    """
    Return all valid 'a' values for Affine Cipher.
    Valid 'a' values are those coprime with 26.
    """
    valid_a = []
    for a in range(1, 26):
        if gcd(a, 26) == 1:
            valid_a.append(a)
    return valid_a

def main():
    """
    Main function to demonstrate Affine Cipher usage.
    """
    print("=" * 60)
    print("AFFINE CIPHER DEMONSTRATION")
    print("=" * 60)
    
    # Display valid 'a' values
    valid_a_values = get_valid_a_values()
    print(f"\nValid 'a' values (coprime with 26): {valid_a_values}")
    print(f"Total valid 'a' values: {len(valid_a_values)}")
    print("Valid 'b' values: 0 to 25\n")
    
    # Example 1: Basic encryption/decryption
    print("EXAMPLE 1: Basic Text")
    print("-" * 40)
    
    plaintext = "HELLO"
    a, b = 5, 8  # Valid keys
    
    print(f"Plaintext:  {plaintext}")
    print(f"Key: a={a}, b={b}")
    
    encrypted = affine_encrypt(plaintext, a, b)
    print(f"Encrypted:  {encrypted}")
    
    decrypted = affine_decrypt(encrypted, a, b)
    print(f"Decrypted:  {decrypted}")
    print(f"Success: {plaintext == decrypted}")
    
    # Example 2: Text with spaces and punctuation
    print("\n" + "=" * 60)
    print("EXAMPLE 2: Text with Spaces and Punctuation")
    print("-" * 40)
    
    plaintext = "Hello, World! 2024"
    a, b = 7, 3  # Another valid key pair
    
    print(f"Plaintext:  {plaintext}")
    print(f"Key: a={a}, b={b}")
    
    # With include_non_alpha=True to preserve spaces and punctuation
    encrypted = affine_encrypt(plaintext, a, b, include_non_alpha=True)
    print(f"Encrypted:  {encrypted}")
    
    decrypted = affine_decrypt(encrypted, a, b, include_non_alpha=True)
    print(f"Decrypted:  {decrypted}")
    print(f"Success: {plaintext.upper() == decrypted.upper()}")
    
    # Example 3: Invalid key demonstration
    print("\n" + "=" * 60)
    print("EXAMPLE 3: Invalid Key Handling")
    print("-" * 40)
    
    plaintext = "TEST"
    a, b = 2, 5  # 2 is not coprime with 26 (gcd(2,26)=2)
    
    print(f"Plaintext:  {plaintext}")
    print(f"Attempting to use invalid key: a={a}, b={b}")
    
    try:
        encrypted = affine_encrypt(plaintext, a, b)
        print(f"Encrypted:  {encrypted}")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Example 4: Interactive demonstration
    print("\n" + "=" * 60)
    print("INTERACTIVE DEMONSTRATION")
    print("-" * 40)
    
    while True:
        print("\nMenu:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Show valid 'a' values")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            text = input("Enter text to encrypt: ")
            try:
                a = int(input("Enter key 'a' (must be coprime with 26): "))
                b = int(input("Enter key 'b' (0-25): "))
                include_non_alpha = input("Preserve non-alphabet characters? (y/n): ").lower() == 'y'
                
                encrypted = affine_encrypt(text, a, b, include_non_alpha)
                print(f"\nEncrypted text: {encrypted}")
                
                # Verify by decrypting
                decrypted = affine_decrypt(encrypted, a, b, include_non_alpha)
                print(f"Decrypted back: {decrypted}")
                
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")
                
        elif choice == '2':
            text = input("Enter text to decrypt: ")
            try:
                a = int(input("Enter key 'a' (must be coprime with 26): "))
                b = int(input("Enter key 'b' (0-25): "))
                include_non_alpha = input("Preserve non-alphabet characters? (y/n): ").lower() == 'y'
                
                decrypted = affine_decrypt(text, a, b, include_non_alpha)
                print(f"\nDecrypted text: {decrypted}")
                
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")
                
        elif choice == '3':
            valid_a = get_valid_a_values()
            print(f"\nValid 'a' values (coprime with 26):")
            print(f"{valid_a}")
            print(f"\nTotal: {len(valid_a)} valid values")
            print("These are numbers where gcd(a, 26) = 1")
            
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()