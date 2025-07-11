def encrypt(message, key):
    encrypted = ""
    for char in message:
        if char.isalnum():  # Letters and digits
            encrypted += chr((ord(char) + key) % 256)
        else:
            encrypted += char  # Keep special characters as-is
    encrypted = encrypted[::-1]  # Reverse the string as a second layer
    return encrypted

def decrypt(encrypted_message, key):
    decrypted = ""
    reversed_msg = encrypted_message[::-1]  # First reverse back
    for char in reversed_msg:
        if char.isalnum():
            decrypted += chr((ord(char) - key) % 256)
        else:
            decrypted += char
    return decrypted

# Main loop
while True:
    print("\nOptions:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == '1':
        message = input("Enter the message to encrypt: ")
        key = int(input("Enter the secret key (integer): "))
        result = encrypt(message, key)
        print("Encrypted Message:", result)

    elif choice == '2':
        message = input("Enter the encrypted message: ")
        key = int(input("Enter the secret key (integer): "))
        result = decrypt(message, key)
        print("Decrypted Message:", result)

    elif choice == '3':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
