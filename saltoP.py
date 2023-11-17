# Para saltos en linea, se utiliza \n
# Abro el archivo en modo Write Extended

archvio = "colores.txt"
f = open(archvio, "w+")

# Escribo 4 lineas adicionales
f.write("Rojo\n")
f.write("Amarillo\n")
f.write("Verde\n")

# Agregando los elementos de una iterable
mas_colores = ["Morado\n", "Celeste\n", "Rosa\n"]
f.writelines(mas_colores)

# cierre el archivo
f.close()
