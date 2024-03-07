def add(x,y):
    return x + y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y==0:
        return "Cannot divide by zero"
    else :
        return x / y
def subtract(x, y):
    return  x - y
print("Select Operatio:")
print("1: Addition")
print("2: Multiplication")
print("3: Division")
print("4: Subtraction")

choice = input("Enter Your operation (1/2/3/4):")

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Your Second Number: "))

if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice =='3':
    result = divide(num1, num2)
    print(f"{num1} / {num2} = {result}")
elif choice =='4':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
else :
    print("Invalid Input")








