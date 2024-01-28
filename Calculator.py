def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero."
    return x / y

def modulas(x, y):
    return x % y

while True :
    print("Menu : ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Remainder")
    print("6. Exit")

    choice = int(input("Enter Choice : "))
    if choice == 6 :
        print("Exit!!")
        break
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))

    while choice != 6:
        if choice == 1:
            print("Result:", add(num1, num2))
        elif choice == 2:
            print("Result:", subtract(num1, num2))
        elif choice == 3:
            print("Result:", multiply(num1, num2))
        elif choice == 4:
            print("Result:", divide(num1, num2))
        elif choice == 5:
            print("Result:", modulas(num1, num2))
        else :
            print("You have entered invalid number!!")
            break

        choice = int(input("Enter Choice : "))
        if choice == 6 :
            break
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number : "))
        
    if choice == 6 :
        print("Exit!!")
        break