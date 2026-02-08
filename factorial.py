def factorial (n):
    product = 1
    for number in range(n, 0, -1):
        product *= number
    return product


print(factorial(int(input('Number: '))))
