from cryptography.fernet import Fernet, InvalidToken
import os

def generate_key():
    """Generate a new encryption key."""
    return Fernet.generate_key()

def save_key(key, filename):
    """Save the encryption key to a file."""
    with open(filename, 'wb') as f:
        f.write(key)

def load_key(filename):
    """Load the encryption key from a file."""
    with open(filename, 'rb') as f:
        return f.read()

def encrypt_file(input_path, output_path, key):
    """Encrypt a file and save the encrypted content to a new file."""
    fernet = Fernet(key)
    
    with open(input_path, 'rb') as f:
        original_data = f.read()
    
    encrypted_data = fernet.encrypt(original_data)
    
    with open(output_path, 'wb') as f:
        f.write(encrypted_data)

def decrypt_file(input_path, output_path, key):
    """Decrypt a file and save the decrypted content to a new file."""
    fernet = Fernet(key)
    
    with open(input_path, 'rb') as f:
        encrypted_data = f.read()
    
    try:
        decrypted_data = fernet.decrypt(encrypted_data)
    except InvalidToken:
        print("Error: Invalid or corrupted key!")
        return False
    
    with open(output_path, 'wb') as f:
        f.write(decrypted_data)
    return True

def main():
    print("File Encryption and Decryption Tool")
    
    while True:
        print("\nOptions:")
        print("1. Generate a new key")
        print("2. Encrypt a file")
        print("3. Decrypt a file")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            key = generate_key()
            key_file = input("Enter filename to save the key: ")
            
            if os.path.exists(key_file):
                overwrite = input("File exists! Overwrite? (y/n): ").lower()
                if overwrite != 'y':
                    continue
            
            save_key(key, key_file)
            print(f"Key saved to {key_file}")

        elif choice == '2':
            input_file = input("Enter file to encrypt: ")
            output_file = input("Enter output filename: ")
            key_file = input("Enter key file: ")
            
            if not os.path.exists(input_file):
                print("Error: Input file not found!")
                continue
            
            if input_file == output_file:
                print("Error: Input and output files must be different!")
                continue
            
            try:
                key = load_key(key_file)
                encrypt_file(input_file, output_file, key)
                print(f"File encrypted successfully: {output_file}")
            except Exception as e:
                print(f"Error: {str(e)}")

        elif choice == '3':
            input_file = input("Enter file to decrypt: ")
            output_file = input("Enter output filename: ")
            key_file = input("Enter key file: ")
            
            if not os.path.exists(input_file):
                print("Error: Input file not found!")
                continue
            
            if input_file == output_file:
                print("Error: Input and output files must be different!")
                continue
            
            try:
                key = load_key(key_file)
                success = decrypt_file(input_file, output_file, key)
                if success:
                    print(f"File decrypted successfully: {output_file}")
            except Exception as e:
                print(f"Error: {str(e)}")

        elif choice == '4':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()