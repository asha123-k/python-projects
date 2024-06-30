def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y
def Floor_division(x, y):
    return x // y
def Modulus( x, y):
    return x % y
def Exponentiation(x, y):
    return x**y
def main():
    print("Welcome to the Simple Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5.Floor_division")
    print("6.Modulus")
    print("7.Exponentiation")
    while True:
        choice = input("Enter choice (1/2/3/4/5/6/7): ")

        if choice in ('1', '2', '3', '4','5','6','7'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")

            elif choice == '5':
                print(f"{num1} // {num2} = {Floor_division(num1, num2)}")

            elif choice == '6':
                print(f"{num1} % {num2} = {Modulus(num1, num2)}")

            elif choice == '7':
                print(f"{num1} ** {num2} = {Exponentiation(num1, num2)}")


            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()
