"""Module random provide an interface for generate of different chars"""
import random
import string


def validate_length(description):
    """Validate input that should return only int value that >= 8"""
    while True:
        length = input(description)
        try:
            if not length.isdigit():
                raise ValueError("Password length should be number")
            if int(length) < 8:
                raise ValueError("Password length should be from 8 symbols")
            return int(length)
        except ValueError as error:
            print(error)


def validate_boolean_input(description):
    """Validate input that should return only bool value"""
    while True:
        value = input(description)
        try:
            if value in ('True', 'T'):
                return True
            if value in ('False', 'F'):
                return False
            raise ValueError("You should select only between True and False")
        except ValueError as error:
            print(error)

class PasswordGenerator:
    """Generate password with different conditions"""

    def __init__(self):
        self.__include_digits = True
        self.__include_special_chars = True
        self.__include_uppercase = True
        self.__include_lowercase = True
        self.__length = 8

    def set_include_digits(self, include_digits):
        """set bool value for private field"""
        self.__include_digits = include_digits

    def set_include_special_chars(self, include_special_chars):
        """set bool value for private field"""
        self.__include_special_chars = include_special_chars

    def set_include_uppercase(self, include_uppercase):
        """set bool value for private field"""
        self.__include_uppercase = include_uppercase

    def set_include_lowercase(self, include_lowercase):
        """set bool value for private field"""
        self.__include_lowercase = include_lowercase

    def set_length(self, length):
        """set int value that represent length of password for private field"""
        self.__length = length

    def generate_password(self):
        """generate password"""
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
