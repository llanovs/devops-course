import random
import string


def validate_length(description):
    while True:
        length = input(description)
        try:
            if not length.isdigit():
                raise ValueError("Password length should be number")
            elif int(length) < 8:
                raise ValueError("Password length should be from 8 symbols")
            else:
                return int(length)
        except Exception as e:
            print(e)


def validate_boolean_input(description):
    while True:
        value = input(description)
        try:
            if value == "True" or value == "T":
                return True
            elif value == "False" or value == "F":
                return False
            else:
                raise ValueError("You should select only between True and False")
        except Exception as e:
            print(e)


class PasswordGenerator:

    def __init__(self):
        self.__include_digits = True
        self.__include_special_chars = True
        self.__include_uppercase = True
        self.__include_lowercase = True
        self.__length = 8

    def set_include_digits(self, include_digits):
        self.__include_digits = include_digits

    def set_include_special_chars(self, include_special_chars):
        self.__include_special_chars = include_special_chars

    def set_include_uppercase(self, include_uppercase):
        self.__include_uppercase = include_uppercase

    def set_include_lowercase(self, include_lowercase):
        self.__include_lowercase = include_lowercase

    def set_length(self, length):
        self.__length = length

    def generate_password(self):
        pattern = ""
        if self.__include_lowercase:
            pattern += string.ascii_lowercase
        if self.__include_uppercase:
            pattern += string.ascii_uppercase
        if self.__include_digits:
            pattern += string.digits
        if self.__include_special_chars:
            pattern += string.punctuation
        generated_string = ''.join([random.choice(pattern) for n in range(self.__length)])
        generated_symbols = list(generated_string)
        random.shuffle(generated_symbols)
        return "".join(str(i) for i in generated_symbols)
