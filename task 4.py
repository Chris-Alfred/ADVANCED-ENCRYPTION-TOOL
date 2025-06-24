from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved to secret.key")

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(file_name, key):
    fernet = Fernet(key)
    with open(file_name, "rb") as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(file_name + ".encrypted", "wb") as encrypted_file:
        encrypted_file.write(encrypted)
    print(f"File encrypted successfully as {file_name}.encrypted")

def decrypt_file(file_name, key):
    fernet = Fernet(key)
    with open(file_name, "rb") as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    output_file = file_name.replace(".encrypted", ".decrypted")
    with open(output_file, "wb") as dec_file:
        dec_file.write(decrypted)
    print(f"File decrypted successfully as {output_file}")


print("\nAdvanced Encryption Tool")
print("--------------------------")
print("1. Generate Key")
print("2. Encrypt File")
print("3. Decrypt File")
choice = input("\nEnter your choice (1/2/3): ")

if choice == '1':
    generate_key()

elif choice == '2':
    key = load_key()
    file_to_encrypt = input("Enter the file name to encrypt: ")
    encrypt_file(file_to_encrypt, key)

elif choice == '3':
    key = load_key()
    file_to_decrypt = input("Enter the file name to decrypt (.encrypted): ")
    decrypt_file(file_to_decrypt, key)

else:
    print("Invalid choice. Please enter 1, 2, or 3.")