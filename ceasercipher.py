def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        # Encrypt/Decrypt only alphabetic characters
        if char.isalpha():
            # Determine the ASCII offset (65 for uppercase, 97 for lowercase)
            ascii_offset = 65 if char.isupper() else 97
            
            # Perform the shift and wrap around using modulo
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            # Non-alphabetic characters are added unchanged
            result += char
            
    return result

def main():
    print("Caesar Cipher Program")
    
    # Get user input for message and shift value
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value (positive for encryption, negative for decryption): "))
    
    # Choose operation
    operation = input("Do you want to encrypt or decrypt the message? (e/d): ").lower()
    
    if operation == 'e':
        encrypted_message = caesar_cipher(message, shift, mode='encrypt')
        print(f"Encrypted Message: {encrypted_message}")
    elif operation == 'd':
        decrypted_message = caesar_cipher(message, shift, mode='decrypt')
        print(f"Decrypted Message: {decrypted_message}")
    else:
        print("Invalid operation. Please choose 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()
