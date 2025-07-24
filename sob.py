"""SOBS included: Sob 28, Sob 29, Sob 30"""


def add(a, b):
    """adds 2 numbers."""
    return a + b


def subtract(a, b):
    """subtracts 2 numbers."""
    return a - b


def multiply(a, b):
    """multiplies 2 number."""
    return a * b


def divide(a, b):
    """divides 2 numbers."""
    if b == 0:
        return "Divison by 0 not allowed." #Problem Statement
    return a / b


def get_number(prompt):
    """gets 2 numbers from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("not a number, enter only a number.")


def main():
    """calculator."""
    while True:
        print("\nhello and welcome to the simple calculator")
        print("select a calculation:")
        print("1.(+)")
        print("2.(-)")
        print("3.(*)")
        print("4.(/)")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Goodbye!")
            break

        if choice in ('1', '2', '3', '4'):
            num1 = get_number("enter a number: ")
            num2 = get_number("Enter another number: ")

            if choice == '1':
                print(f"result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"result: {num1} / {num2} = {divide(num1, num2)}")
        else:
            print("not a choice.")

if __name__ == "__main__":
    main()
