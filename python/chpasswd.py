import os
import re
import random
import string
import subprocess


def main():
    print("Password change for Linux User")
    username = input("Please enter a username: ")
    validate_username(username)
    new_password = create_new_password()
    update_password(username, new_password)


def validate_input(psw_length):
    if not psw_length.isdigit():
        raise ValueError("Password length should be number")
    elif int(psw_length) < 6:
        raise ValueError("Password length too small. Please use password length from 6 symbols")


def select_operation():
    return int(input(
        """Please select an operation:
        1. Create a password
        2. Generate a password
        """))


def create_new_password():
    operation = select_operation()
    if operation == 1:
        new_password = input("Please enter a password: ")
        validate_new_password(new_password)
        return new_password
    else:
        password_length = input("Please enter a password desirable password length (minimum is 6): ")
        return generate_password(int(password_length))


def generate_password(psw_length):
    generated_string = ''.join([random.choice(string.ascii_lowercase + string.ascii_uppercase
                                              + string.digits + string.punctuation) for n in range(psw_length)])
    generated_symbols = list(generated_string)
    random.shuffle(generated_symbols)
    return "".join(str(i) for i in generated_symbols)


def validate_new_password(new_password):
    special_characters = "[@_!#$%^&*()<>?/|}{~:]"
    if len(new_password) < 6:
        raise ValueError("Password length should be at least 6.")
    elif not bool(re.search(r'\d', new_password)):
        raise ValueError("Password should contain at least one digit.")
    elif not bool(new_password in special_characters.split("")):
        raise ValueError("Password should contain at least one special character.")
    elif not bool(re.search(r'a-z', new_password)):
        raise ValueError("Password should contain at least one lowercase letter.")
    elif not bool(re.search(r'A-Z', new_password)):
        raise ValueError("Password should contain at least one uppercase letter.")


def validate_username(username):
    all_users = subprocess.Popen("cat /etc/passwd".split(" "), text=True, stdout=subprocess.PIPE)
    final_process = subprocess.Popen("tr \";\" \"\n\"".split(" "), stdin=all_users.stdout, stdout=subprocess.PIPE, text=True)
    grep_process = subprocess.Popen(["grep", "\\" + username + "\\b"], stdin=final_process.stdout, stdout=subprocess.PIPE, text=True)
    output, error = grep_process.communicate()
    if username in output:
        print("User exist")
    else:
        raise ValueError("User doesn't exist")


def update_password(username, new_password):
    update_process = subprocess.Popen(['/usr/bin/sudo', '/usr/bin/passwd', username], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    password = (new_password + "\n" + new_password).encode('utf-8')
    update_process.communicate(password)
    print("User: " + username + ". Updated password: " + new_password)


if __name__ == "__main__":
    main()
