def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def Calculate():
    num1 = int(input("Enter Num1: "))
    num2 = int(input("Enter Num2: "))
    operation = input("Enter operation: ")
    if(operation == '+'):
        result = addition(num1, num2)
    elif(operation == '-'):
        result = subtraction(num1, num2)
    elif(operation == '*'):
        result = multiplication(num1, num2)
    elif(operation == '/'):
        result = division(num1, num2)
    else:
        result = 'INVALID CHOICE'
    # entry = result
    print("Result is: ", result)


if __name__ == '__main__':
    Calculate()
