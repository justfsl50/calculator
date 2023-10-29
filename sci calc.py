import math

print("Welcome to the Scientific Calculator!")
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponentiation")
print("6. Square Root")

while True:
    choice = input("Enter operation number (1-6): ")
    if choice in ('1', '2', '3', '4', '5', '6'):
        break
    else:
        print("Invalid input. Please try again.")

if choice == '1':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(num1, "+", num2, "=", num1 + num2)

elif choice == '2':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(num1, "-", num2, "=", num1 - num2)

elif choice == '3':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(num1, "*", num2, "=", num1 * num2)

elif choice == '4':
    num1 = float(input("Enter divident: "))
    num2 = float(input("Enter divisor: "))
    print(num1, "/", num2, "=", num1 / num2)

elif choice == '5':
    num1 = float(input("Enter base: "))
    num2 = float(input("Enter exponent: "))
    print(num1, "^", num2, "=", num1 ** num2)

elif choice == '6':
    num = float(input("Enter number: "))
    print("sqrt(", num, ")=", math.sqrt(num))

else:
    print("Invalid input. Please try again.")
