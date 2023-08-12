def main():
    print("Welcome to the Calculator Program!")

    calculator = create_calculator()
    print_possible_operations()

    operation = int(input("Enter your choice (1-4): "))

    result = calculate(operation, calculator)
    print("The result of multiplication is: " + str(result))


def calculate(operation, calculator):
    return {
        1: calculator.addition(),
        2: calculator.subtraction(),
        3: calculator.multiplication(),
        4: calculator.division()
    }[operation]


def create_calculator():
    number1 = int(input("Please enter the first number: "))
    number2 = int(input("Please enter the second number: "))
    return Calculator(number1, number2)


def print_possible_operations():
    print(
        """Please select an operation:
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division""")


class Calculator:

    def __init__(self, number1, number2):
        self._number1 = number1
        self._number2 = number2

    def addition(self):
        return self._number1 + self._number2

    def subtraction(self):
        return self._number1 - self._number2

    def multiplication(self):
        return self._number1 * self._number2

    def division(self):
        if self._number2 == 0:
            print("Cannot divide by 0")
        else:
            return self._number1 // self._number2


if __name__ == "__main__":
    main()
