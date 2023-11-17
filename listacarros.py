# lISTA A ESCRIBIR EN UN ARCHIVO.

marcas = ["Audi\n", "Alfa Romeo\n", "Mercedes Benz\n"]

# Se Abre en modo Whrite Extended, que permite lectura.

with open("marcas.txt", "w+") as f:
    # Escribir cada elemento de la lista como en linea.
    f.writelines(marcas)
    # Se va al inicio del archivo
    f.seek(0, 0)
    # Lee secuencialmente el archivo,desde el inicio.
    for linea in f:
        print(linea)
