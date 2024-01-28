import hashlib
import getpass

class PasswordManager:
    PASSWORD_FILE = "/Users/macbookpro13/Desktop/FOCP Task 1-3/Task 3/password.txt"

    def __init__(self):
        self.user_data = self.load_user_data()

    def load_user_data(self):
        try:
            with open(self.PASSWORD_FILE, 'r') as file:
                return file.read().strip().split('\n')
        except FileNotFoundError:
            print("Password file not found. Starting with an empty list.")
            return []

    def save_user_data(self):
        with open(self.PASSWORD_FILE, 'w') as file:
            file.write('\n'.join(self.user_data))

    def encrypt_password(self, password):
        return hashlib.md5(password.encode()).hexdigest()

    def find_user(self, username):
        for user in self.user_data:
            if user.split(':')[0] == username:
                return user
        return None

    def add_user(self):
        username = input("Enter new username: ").strip()
        if self.find_user(username):
            print("Username already exists.")
            return

        real_name = input("Enter real name: ").strip()
        password = self.encrypt_password(getpass.getpass("Enter password: "))
        self.user_data.append(f"{username}:{real_name}:{password}")
        self.save_user_data()
        print("User added.")

    def delete_user(self):
        username = input("Enter username to delete: ").strip()
        user = self.find_user(username)
        if user:
            if input("Confirm deletion (y/n): ").lower() == 'y':
                self.user_data.remove(user)
                self.save_user_data()
                print("User deleted.")
            else:
                print("Deletion cancelled.")
        else:
            print("User not found.")

    def change_password(self):
        username = input("Username: ").strip()
        user = self.find_user(username)
        if user:
            current_password = self.encrypt_password(getpass.getpass("Current password: "))
            if current_password == user.split(':')[2]:
                new_password = self.encrypt_password(getpass.getpass("New password: "))
                confirm_password = self.encrypt_password(getpass.getpass("Confirm new password: "))
                if new_password == confirm_password:
                    self.user_data[self.user_data.index(user)] = f"{username}:{user.split(':')[1]}:{new_password}"
                    self.save_user_data()
                    print("Password changed.")
                else:
                    print("Passwords do not match.")
            else:
                print("Incorrect current password.")
        else:
            print("User not found.")

    def login(self):
        username = input("Username: ").strip()
        password = self.encrypt_password(getpass.getpass("Password: "))
        user = self.find_user(username)
        if user and password == user.split(':')[2]:
            print("Login successful.")
        else:
            print("Login failed.")

if __name__ == "__main__":
    manager = PasswordManager()
    actions = {"1": manager.add_user, "2": manager.delete_user, "3": manager.change_password, "4": manager.login}

    while True:
        print("\nChoose an option:\n1. Add User\n2. Delete User\n3. Change Password\n4. Login\n5. Exit")
        choice = input("Your choice: ")
        if choice in actions:
            actions[choice]()
        elif choice == "5":
            break
        else:
            print("Invalid choice, please enter a number between 1 and 5.")

