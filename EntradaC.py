import os
Entrada = [
    ['correo', 'nombre', 'telefono'],
    ['juan@gmail.com', 'Juan', '8123232323232'],
    ['maria@gmail.com', 'Maria', '554545454545'],
    ['diana@gmail.com', 'Diana', '449090090909']
]

with open("agenda.csv", "w+") as f:
    for e in Entrada:
        f.write((f'{e[0]}|{e[1]}|{e[2]}\n'))

# Se imprime el contenido de la lista, para cotejar.
print(">> Contenido de la lista.\n")
print(Entrada)
# Revisa si existe el CSV, en cuyo caso, si existe el BAK lo elimina
# y renombra el CSV como BAK
if os.path.exists("agenda.csv"):
    if (os.path.exists("agenda.bak")):
        os.remove("agenda.bak")
        os.rename("agenda.csv", "agenda.bak")
# Se escribe el contenido de la lista, usando with y F-String
with open("agenda.csv", "w+") as f:
    for e in Entrada:
        f.write(f"{e[0]}|{e[1]}|{e[2]}\n")
# Se revisa el contenido del archivo.
print("\n>> Contenido del archivo.\n")
with open("agenda.csv") as f:
    print(f.read())
