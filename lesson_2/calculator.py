# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.

print('Welcome to Calculator!')

print('What is the first number?')
number1 = int(input())
print('What is the second number?')
number2 = int(input())

print('What operation would you like to perform?\n'
      '1) Add 2) Substract 3) Multiply 4) Divide')
operation = input()
result = 0

match operation:
    case '1':
        result = number1 + number2
    case '2':
        result = number1 - number2
    case '3':
        result = number1 * number2
    case '4':
        result = number1 / number2

print(f'The result is:\n{result}')
