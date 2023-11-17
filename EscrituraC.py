# Abro el archivo en mod Write Extended
# Si el archivo existe, lo genera. Si existe ,lo remplaza.
# Los contenidos van en secuencia

archivo = "colores.txt"
f = open(archivo, "+w")

# Escribir 4 contenidos en secuencia
f.write("Blanco")
f.write("Negro")
f.write("Naranja")

# cierre el archivo
f.close
