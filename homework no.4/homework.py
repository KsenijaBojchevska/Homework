
# function add two numbers
def add_num(x, y):
    sum = x+y
    return sum

# function subtracts two numbers


def subtract_num(x, y):
    subtract = x-y
    return subtract

# This function multiplies two numbers


def multiply_num(x, y):
    multiply = x*y
    return multiply

# This function divides two numbers


def divide_num(x, y):
    if y == 0:
        print("You can not devide with zero")
    devide = x/y
    return devide


# this is msg for choose
def printMsq():
    print("\nSelect operation. \n"
          "1.Add\n"
          "2.Subtract\n"
          "3.Multiply\n"
          "4.Divide")


# print msg
printMsq()

# this is input from the user
choice = int(input("Enter choice: (1/2/3/4):"))
no1 = float(input("Enter first number: "))
no2 = float(input("Enter second number: "))


# this is choise for def functions
if choice == 1:
    print(no1, "+", no2, "=",
          add_num(no1, no2))

elif choice == 2:
    print(no1, "-", no2, "=",
          subtract_num(no1, no2))

elif choice == 3:
    print(no1, "*", no2, "=",
          multiply_num(no1, no2))

elif choice == 4:
    print(no1, "/", no2, "=",
          divide_num(no1, no2))
else:
    print("Invalid input")

# msq for breaking or continue
msgForContinuing = input("Would you like to do a new calculation? (yes/no): ")


while True:
    if msgForContinuing == "no":
        break
    elif msgForContinuing == "yes":
        continue
