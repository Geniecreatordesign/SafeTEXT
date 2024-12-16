import base64
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from colorama import Fore, Style, init  # Pastikan untuk mengimpor colorama

# Initialize colorama
init(autoreset=True)

# Function to adjust border length based on terminal size
def adjust_border():
    try:
        # Get terminal width
        width = os.get_terminal_size().columns
        return min(width, 80)  # Limit maximum border length to 80
    except OSError:
        # Default border length if terminal size cannot be determined
        return 50

# Panjang border atas dan bawah
border_length = adjust_border()

# Function to center text based on terminal width
def center_text(text, width):
    return " " * ((width - len(text)) // 2) + text

# Display header
print(Fore.GREEN + Style.BRIGHT + "=" * border_length)
print(Fore.YELLOW + Style.BRIGHT + center_text("Welcome", border_length))
print(Fore.YELLOW + Style.BRIGHT + center_text("S a f e T E X T", border_length))
print(Fore.GREEN + Style.BRIGHT + "=" * border_length)
print()

# Function to generate a random 5-character unique code
def generate_unique_code():
    return base64.urlsafe_b64encode(os.urandom(4))[:5].decode()

# Function to derive AES-256 key using PBKDF2
def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # 256-bit key for AES-256
        salt=salt,
        iterations=100_000,
        backend=default_backend()
    )
    return kdf.derive(password)

# Function to encrypt text
def encrypt_text():
    text = input("Input Your Text: ").encode()  # Changed here
    password = input("Enter a password for encryption: ").encode()

    # Generate salt and AES key
    salt = os.urandom(16)
    key = derive_key(password, salt)

    # Encrypt the text
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_text = encryptor.update(text) + encryptor.finalize()

    # Generate a unique 5-character code
    unique_code = generate_unique_code()

    # Combine encrypted text, IV, and salt
    combined = base64.urlsafe_b64encode(salt + iv + encrypted_text).decode()

    print(Fore.GREEN + Style.BRIGHT + "Encryption successful!")
    print(f"Your unique code: {Fore.CYAN + unique_code}")
    print(f"Your SafeTEXT: {Fore.CYAN + combined}")

    return combined, unique_code

# Function to decrypt text
def decrypt_text():
    try:
        encrypted_data = input("Enter Your SafeTEXT: ").encode()  # Changed here
        unique_code = input("Enter the unique code: ")
        password = input("Enter the password: ").encode()

        # Decode the encrypted data
        combined = base64.urlsafe_b64decode(encrypted_data)
        salt, iv, encrypted_text = combined[:16], combined[16:32], combined[32:]

        # Derive key from password and salt
        key = derive_key(password, salt)

        # Decrypt the text
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_text = decryptor.update(encrypted_text) + decryptor.finalize()

        print(Fore.GREEN + "Decryption successful!")
        print(f"Decrypted text: {decrypted_text.decode()}")
    except (ValueError, Exception) as e:
        print(Fore.RED + "Decryption failed. Invalid password or encrypted text.")

# Main loop
while True:
    print("\n" + Fore.YELLOW + "--- Menu ---")
    print(Fore.YELLOW + "1. Input Your Text")  # Changed here
    print(Fore.YELLOW + "2. Your SafeTEXT")  # Changed here (removed the colon)
    print(Fore.YELLOW + "3. Exit")
    choice = input(Fore.CYAN + "Choose an option (1/2/3): ")

    if choice == '1':
        encrypt_text()
    elif choice == '2':
        decrypt_text()
    elif choice == '3':
        os.system('clear')  # Clear the screen
        print(Fore.CYAN + "Exiting...")
        break
    else:
        print(Fore.RED + "Invalid choice. Please try again.")

# Closing message in different languages with emojis
print("\n" + Fore.CYAN + "Terima Kasih! 🐱", end=" ")
print(Fore.GREEN + "谢谢! 🐼", end=" ")
print(Fore.YELLOW + "Спасибо! 🐶", end=" ")
print(Fore.GREEN + "Merci! 🐰", end=" ")
print(Fore.CYAN + "شكراً! 🦊", end=" ")
print(Fore.YELLOW + "Obrigado! 🐨", end=" ")
print(Fore.GREEN + "Dank je wel! 🦋", end=" ")
print(Fore.CYAN + "ありがとうございます! 🐥", end=" ")
print(Fore.GREEN + "Obrigado! 🐧", end=" ")
print(Fore.CYAN + "¡Gracias! 🐢")
