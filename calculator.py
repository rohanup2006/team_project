def multiply(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

def floor_division(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a //b
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def power(a, b):
    return a ** b

print("1. Addition")
print("2. Subtraction")
print("3. Power")

choice = input("Enter your choice (1-3): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "1":
    print("Result =", add(num1, num2))

elif choice == "2":
    print("Result =", subtract(num1, num2))

elif choice == "3":
    print("Result =", power(num1, num2))

else:
    print("Invalid choice!")