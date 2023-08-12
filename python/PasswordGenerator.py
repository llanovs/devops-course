import random
import string


def main():
    print("Welcome to the Linux User Password Generator!")
    psw_length = input("Please enter the desired password length: ")
    validate_inout(psw_length)
    generated_psw = generate(int(psw_length))
    print("Generated password: " + str(generated_psw))


def validate_inout(psw_length):
    if not psw_length.isdigit():
        raise ValueError("Password length should be number")
    elif int(psw_length) < 4:
        raise ValueError("Password length too small. Please use password length from 5 symbols")


def generate(psw_length: int):
    generated_string = ''.join([random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation) for n in range(psw_length)])
    generated_symbols = list(generated_string)
    random.shuffle(generated_symbols)
    return "".join(str(i) for i in generated_symbols)


if __name__ == "__main__":
    main()
