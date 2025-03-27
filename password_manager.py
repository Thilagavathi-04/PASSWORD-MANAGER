from cryptography.fernet import Fernet

# Function to generate and save a key (Run only once!)
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Uncomment and run once to generate the key, then comment it out!
# write_key()

# Function to load the encryption key from the key file
def load_key():
    return open("key.key", "rb").read()

# Load the existing key
key = load_key()
fernet = Fernet(key)

# Function to save an encrypted password
def save_password(website, username, password):
    encrypted_pass = fernet.encrypt(password.encode()).decode()  # Encrypt the password
    with open("passwords.txt", "a") as file:  # Open file in append mode
        file.write(f"{website}|{username}|{encrypted_pass}\n")  # Save encrypted data
    print("Password saved successfully!")

# Function to view and decrypt saved passwords
def view_passwords():
    try:
        with open("passwords.txt", "r") as file:
            for line in file.readlines():
                website, username, encrypted_pass = line.strip().split("|")
                decrypted_pass = fernet.decrypt(encrypted_pass.encode()).decode()  # Decrypt the password
                print(f"Website: {website}, Username: {username}, Password: {decrypted_pass}")
    except FileNotFoundError:
        print("No passwords saved yet!")

# Main menu loop
while True:
    choice = input("\nDo you want to (1) Save a password or (2) View passwords? (q to quit): ")

    if choice == "1":
        site = input("Enter website: ")
        user = input("Enter username: ")
        pwd = input("Enter password: ")
        save_password(site, user, pwd)  # Save encrypted password

    elif choice == "2":
        view_passwords()  # View decrypted passwords

    elif choice.lower() == "q":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or q.")
