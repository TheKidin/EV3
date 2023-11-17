# Abro el archivo en modo lectura
archivo = "colores.txt"
f = open(archivo, "r")

# leo unicamente la primera linea del archivo
contenido = f.readline()
# Muestra el contenido
print(contenido)

# leo siguiente linea
contenido = f.readline()
# Muestra el contenido
print(contenido)

# cierre el archivo
f.close()
