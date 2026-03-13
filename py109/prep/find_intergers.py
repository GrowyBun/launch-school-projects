def find_integers(my_tuple):
        return [ element
                for element in my_tuple
                if type(element) is int ]

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)
print(integers)                    # [1, 3, -4]