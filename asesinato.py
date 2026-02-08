jugadores = [
    'ikura',
    'gato',
    'laura',
    'bareto',
    'gamiemia',
    'navas',
    'daniel',
    'pipe',
    'checho',
    'emyi',
    'fede',
    'gabriela r',
]

items = [
    'copa',
    'papel higienico',
    'gafas',
    'control',
    'tenedor',
    'lata',
    'cuchara', 
    'maletin',
    'paraguas',
    'media',
    'bolsa',
    'naipes',
]

lugares = [
    'cocina',
    'balcon',
    'bano',
    'cuarto principal',
    'pasillo',
    'meson',
    'cuarto auxiliar',
    'cama',
    'cocina',
    'balcon',
    'bano',
    'cuarto principal'
]

target = [
    'gabriela',
    'daniel',
    'bareto',
    'gamiemia',
    'navas',
    'gato',
    'pipe',
    'ikura',
    'laura',
    'checho',
    'emyi',
    'fede',
]
ziped_lists = zip(items, lugares, target)
index = 0
for i in ziped_lists:
    print(jugadores[index])
    input('ready?: ')
    print({i})
    input('next: ')
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    index += 1



    