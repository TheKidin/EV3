# Se abre un archivo en modo Appen Extended (a+). si el archivo
# no existe, lo crea, con caopacidad de lectura y escritura. el
# apuntador de escritura se coloca al final del archivo

import os

archivo = "colores.txt"
f = open(archivo, "a+")

# verificar de que ya se creo

if os.path.exists(archivo):
    print("\nEl Archivo ya existe")
else:
    print("\nEl Archivo no existe")

# Se cierra el archivo
f.close()
