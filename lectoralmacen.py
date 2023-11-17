archi1 = open("datos.txt", "r")
lineas = archi1.readlines()
print('El archivo tiene', len(lineas), 'lineas')
print('El contenido del archivo')
for linea in lineas:
    print(lineas, end='')
archi1.close()
