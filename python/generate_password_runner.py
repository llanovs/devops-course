"""Module provide an interface for password_generator"""
from password_generator import validate_length, validate_boolean_input, PasswordGenerator

print("Welcome to the Linux User Password Generator!")

LENGTH = validate_length("Please enter the desired password length: ")
INCLUDE_DIGITS = validate_boolean_input("Do you want to include digits? T(True) or F(False) ")
INCLUDE_SPECIAL_CHARS = validate_boolean_input("Include special chars? True or False ")
INCLUDE_UPPERCASE = validate_boolean_input("Include uppercase letters? True or False ")
INCLUDE_LOWERCASE = validate_boolean_input("Include lowercase letters? True or False ")

password_generator = PasswordGenerator()
password_generator.set_length(LENGTH)
password_generator.set_include_lowercase(INCLUDE_LOWERCASE)
password_generator.set_include_uppercase(INCLUDE_UPPERCASE)
password_generator.set_include_digits(INCLUDE_DIGITS)
password_generator.set_include_special_chars(INCLUDE_SPECIAL_CHARS)

GENERATED_PASSWORD = password_generator.generate_password()
print("Generated password: " + GENERATED_PASSWORD)
