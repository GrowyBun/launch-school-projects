age = int(input('How old are you? '))
year = 10
i = 0
print(f'You are {age} years old.')
while (i < 4):
    age += 10
    print(f'In {year} years, you will be {age} years old.')
    year += 10
    i += 1
