names = {'Alice': 'USA', 'Francois': 'Canada', 'Inti': 'Peru'}

def get_country(name):
    return names[name]

print(get_country(input('Name: ')))