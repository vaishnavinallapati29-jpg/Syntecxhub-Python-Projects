
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b


def calculator():
    print("\n===== SIMPLE CALCULATOR =====")

    while True:
        print("\n1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Clear / Start Again")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "6":
            print("Thank you for using the calculator!")
            break

        if choice == "5":
            print("Calculator cleared.")
            continue

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please try again.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                result = add(a, b)
            elif choice == "2":
                result = subtract(a, b)
            elif choice == "3":
                result = multiply(a, b)
            else:
                result = divide(a, b)

            print("Result:", result)

        except ValueError:
            print("Invalid input! Please enter numbers.")


if __name__ == "__main__":
    calculator()
