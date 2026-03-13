input_dict = { "a": [1, 2, 3], "b": [4, 5, 6] }
# Transformed Dict: { "a": [0, 0, 0], "b": [0, 0, 0] }

def non_mutating_transform(my_dict):
    return { key: [0] * len(value) for key, value in my_dict.items() }

def partial_mutating_transform(my_dict):
    for key in my_dict.keys():
        my_dict[key] = [0] * len(my_dict[key])
    return my_dict
def mutating_transform(my_dict):
    for key, value in my_dict.items():
        my_dict[key] = [ 0 for num in value ]
    return my_dict

print(non_mutating_transform(input_dict))
print(input_dict)
print(mutating_transform(input_dict))
print(input_dict)