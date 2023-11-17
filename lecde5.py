# Abro el archivo en modo lectura
archivo = "colores.txt"
f = open(archivo, "r")

# Leo unicamente los primeros 5 caracteres del archivo
contenido = f.read(5)
# Muestro el contenido
print(contenido)

# leo otros 5 caracteres del archivo
contenido = f.read(5)
# Muestro el contenido
print(contenido)

# cierre el archivo
f.close()
