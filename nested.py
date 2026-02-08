my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

index = 0
while index < len(my_list):
    sub_index = 0
    while sub_index < len(my_list[index]):
        number = my_list[index][sub_index]
        if number % 2 == 0:
            print(number)
        
        sub_index += 1

    index += 1

            