import hashlib
from cryptography.fernet import Fernet
import os


def generate_key(master_pwd):
    # Generate a key using the master password
    return Fernet.generate_key()


def load_or_generate_key(master_pwd):
    key_path = "key.key"
    if os.path.exists(key_path):
        with open(key_path, "rb") as key_file:
            key = key_file.read()
    else:
        key = generate_key(master_pwd)
        with open(key_path, "wb") as key_file:
            key_file.write(key)
    return key


def encrypt_data(data, key):
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data


def decrypt_data(encrypted_data, key):
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    return decrypted_data


def view(key):
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split(" ")
            print("User:", user, ", Password:", decrypt_data(passw.encode(), key))


def add(key):
    name = input("Account Name:")
    pwd = input("Password:")
    encrypted_pwd = encrypt_data(pwd, key)

    with open("passwords.txt", 'a') as f:
        f.write(name + " " + encrypted_pwd.decode() + "\n")


def create_master_password():
    while True:
        master_pwd = input("Create a master password: ")
        confirm_pwd = input("Confirm master password: ")
        if master_pwd == confirm_pwd:
            # Hash the master password before storing
            hashed_pwd = hashlib.sha256(master_pwd.encode()).hexdigest()
            with open("master_password.txt", "w") as f:
                f.write(hashed_pwd)
            print("Master password set successfully.")
            break
        else:
            print("Passwords do not match. Please try again.")


def reset_master_password():
    create_master_password()


def authenticate_master_password():
    if not os.path.exists("master_password.txt"):
        create_master_password()

    stored_hashed_pwd = None
    with open("master_password.txt", "r") as f:
        stored_hashed_pwd = f.read().strip()

    while True:
        entered_pwd = input("Enter the master password: ")
        entered_hashed_pwd = hashlib.sha256(entered_pwd.encode()).hexdigest()
        if entered_hashed_pwd == stored_hashed_pwd:
            # Generate or load key based on master password
            key = load_or_generate_key(entered_pwd)
            return key
        elif entered_pwd.lower() == "reset":
            reset_master_password()
            stored_hashed_pwd = None
            with open("master_password.txt", "r") as f:
                stored_hashed_pwd = f.read().strip()
        else:
            print("Incorrect master password. Please try again or type 'reset' to reset the master password.")


def main():
    key = authenticate_master_password()
    while True:
        mode = input(
            "Would you like to add a new password or view existing ones? (view or add): Press q to quit ").lower()
        if mode == 'q':
            break

        if mode == "view":
            view(key)

        elif mode == "add":
            add(key)

        else:
            print("Invalid mode.")
            continue


if __name__ == "__main__":
    main()
