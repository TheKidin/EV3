archivo = "colores.txt"
f = open(archivo, "+a")

# Agregar los elementos de una iterable
mas_colores = ["Morado\n", "Celeste\n", "Rosa\n"]
f.writelines(mas_colores)

# Cierra el archivo
f.close()
