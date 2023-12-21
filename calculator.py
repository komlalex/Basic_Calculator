# Define the functions needed: add, sub, mul, div
# print options to the user
# ask for values
# call the functions 
# while loop to continue the orogram until the user wants to exit

def add(a, b):
    answer = a + b
    print(f"a + b = {answer}")

def sub(a, b):
    answer = a - b
    print(f"a - b = {answer}")

def mul(a, b):
    answer = a * b
    print(f"a x b = {answer}")

def div(a, b):
    answer = a / b
    print(f"a ÷ b = {answer}")

print("Welcome to Kalculator")

while True:
    print("What operation do you want to perform: ")
    print("A -> Addition")
    print("B -> Subtraction")
    print("C -> Multiplication")
    print("D -> Division")
    print("E -> Exit")

    choice = str(input("Input your choice: \n"))

    choice = choice.lower()

    if choice == "a" :
        print("Addition")
        a = int(input("First number: \n"))
        b = int(input("Second number: \n"))
        add(a, b)
    elif choice == "b":
        print("Subtraction")
        a = int(input("First number: \n"))
        b = int(input('Second number: \n'))
        sub(a, b)
    elif choice == "c":
        print("Multiplication")
        a = int(input("First number: \n"))
        b = int(input("Second number: \n"))
        mul(a, b)
    elif choice == "d":
        print("Division")
        a = int(input("First number: \n"))
        b = int(input("Second number: \n"))
        div(a, b)
    elif choice == "e":
        print("Thank you for using Kalculator.")
        quit()
    else:
        print(f"{choice} is not a valid option.")

