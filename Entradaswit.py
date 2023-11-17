Entrada = [
    ['correo', 'nombre', 'telefono'],
    ['juan@gmail.com', 'Juan', '8123232323232'],
    ['maria@gmail.com', 'Maria', '554545454545'],
    ['diana@gmail.com', 'Diana', '449090090909']
]

with open("agenda.csv", "w+") as f:
    for e in Entrada:
        f.write((f'{e[0]}|{e[1]}|{e[2]}\n'))
