def sum(a, b):
    return (a + b)
operation = int(input('1 = multiplication, 2 = division, 3 = addition, 4 = subtraction'))
if operation == 1:
    num1 = float(input('first number:'))
    num2 = float(input('second number:'))
    print(f'the product of {num1} and {num2} is {num1 * num2}')
if operation == 2:
    num1 = float(input('first number:'))
    num2 = float(input('second number:'))
    print(f'the dividend of {num1} and {num2} is {num1 / num2}')
if operation == 3:
    num1 = float(input('first number:'))
    num2 = float(input('second number:'))
    print(f'the product of {num1} and {num2} is {sum(num1, num2)}')
if operation == 4:
    num1 = float(input('first number:'))
    num2 = float(input('second number:'))
    print(f'the product of {num1} and {num2} is {num1 - num2}')
