from PasswordGenerator import PasswordGenerator, validate_length, validate_boolean_input

print("Welcome to the Linux User Password Generator!")

psw_length = validate_length("Please enter the desired password length: ")
psw_include_digits = validate_boolean_input("Do you want to include digits? T(True) or F(False) ")
psw_include_special_chars = validate_boolean_input("Do you want to include special chars? T(True) or F(False) ")
psw_include_uppercase = validate_boolean_input("Do you want to include uppercase letters? T(True) or F(False) ")
psw_include_lowercase = validate_boolean_input("Do you want to include lowercase letters? T(True) or F(False) ")

password_generator = PasswordGenerator()
password_generator.set_length(psw_length)
password_generator.set_include_lowercase(psw_include_lowercase)
password_generator.set_include_uppercase(psw_include_uppercase)
password_generator.set_include_digits(psw_include_digits)
password_generator.set_include_special_chars(psw_include_special_chars)

generated_password = password_generator.generate_password()
print("Generated password: " + generated_password)
