def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def modulus(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a % b

def power(a, b):
    return a ** b


while True:
    print("\n===== RISHABH CALCULATOR =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Modulus (%)")
    print("4. Power (**)")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("Calculator Closed.")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid Choice!")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print("Result =", add(num1, num2))

    elif choice == "2":
        print("Result =", subtract(num1, num2))

    elif choice == "3":
        print("Result =", modulus(num1, num2))

    elif choice == "4":
        print("Result =", power(num1, num2))