## Caesar Cipher Script

### Overview
The **Caesar Cipher Script** is a simple implementation of the classic Caesar cipher encryption and decryption technique. This script allows users to securely encode and decode messages by shifting the letters of the alphabet by a specified number of positions. It supports both encryption and decryption operations, making it a versatile tool for basic cryptography.

### Features
- **Encryption and Decryption**: Easily encrypt messages by shifting letters forward or decrypt them by shifting letters backward.
- **User-Friendly Interface**: Interactive command-line interface that prompts users for input.
- **Handles Non-Alphabetic Characters**: Preserves non-alphabetic characters (such as spaces, punctuation, etc.) in their original form during encryption and decryption.

### How It Works
The script defines a function `caesar_cipher(text, shift, mode)` that processes the input text based on the specified shift value and mode (either 'encrypt' or 'decrypt'). The function works as follows:
1. It checks if the mode is 'decrypt' and adjusts the shift value accordingly.
2. It iterates through each character in the input text:
   - If the character is an alphabetic letter, it calculates its new position based on the ASCII value, applying the shift and wrapping around using modulo arithmetic.
   - Non-alphabetic characters are added to the result unchanged.
3. The final encrypted or decrypted message is returned.

### Usage Instructions

#### Prerequisites
- Ensure you have Python 3.x installed on your machine.

#### Running the Script
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/yourproject.git
   ```
2. Navigate into the project directory:
   ```bash
   cd yourproject
   ```
3. Run the script using Python:
   ```bash
   python caesar_cipher.py
   ```

#### User Interaction
After running the script, follow these prompts:
1. Enter the message you want to encrypt or decrypt.
2. Specify the shift value:
   - Use a positive number for encryption (e.g., a shift of 3 will convert 'A' to 'D').
   - Use a negative number for decryption (e.g., a shift of -3 will convert 'D' back to 'A').
3. Choose whether to encrypt or decrypt by entering 'e' or 'd'.

### Example
```plaintext
Caesar Cipher Program
Enter the message: Hello, World!
Enter the shift value (positive for encryption, negative for decryption): 3
Do you want to encrypt or decrypt the message? (e/d): e
Encrypted Message: Khoor, Zruog!
```

### Contact
For questions or suggestions, please reach out to SiDisUniquE at siddharthban21@gmail.com.
