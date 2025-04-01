def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

n1 = float(input("What's the first number? "))

current_result = 0
end_calc = False

while not end_calc: 
    operation = input("What's the operation? ")
    n2 = float(input("What's the next number? "))

    for symbol in operations:
        current_result = operations[operation](n1, n2)

    print(current_result)
    keep_loop = input(f"Type 'y' if you want to continue calculating with {current_result} and 'n' if you want to quit ")
    
    if keep_loop == "y":
        n1 = current_result
    else:
        end_calc = True