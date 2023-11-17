# Abro el archivo en modo lectura

archivo = "colores.txt"
f = open(archivo, "r")

# leo el contenido y se lo asigno a la variable
contenido = f.read()

# Muestra el contenido. Debe ser todo el archivo
print(contenido)

# cierro el archivo
f.close()
