# abro el archivo modo lectura
archivo = "colores.txt"
f = open(archivo, "r")
# leo unicamente los primeros 5 caracteres del archivo
for linea in f:
    print(">", linea)
# cierre el archivo
f.close()
