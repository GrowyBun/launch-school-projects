def add_to_list_safely(item, target_list=None):
    if target_list is None:
        target_list = []  # A new list is created for each call
    target_list.append(item)
    return target_list

list_a = add_to_list_safely("A")
print(list_a)

list_b = add_to_list_safely("B")
print(list_b)