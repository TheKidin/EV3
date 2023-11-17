with open("colores.txt", "r") as f:
    contenido = f.read()
    print(contenido)

# comporbamos que,aun que no se aplico el colse(), el archivo
# esta cerrado

print("¿Archivo cerrado?", f.closed)
