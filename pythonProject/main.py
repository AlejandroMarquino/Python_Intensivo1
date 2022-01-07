""" Enunciado:  Imprime todos los ficheros existentes en tu carpeta de Descargas.
    El algoritmo del ejercicio es el siguiente:
- Obtén todos los ficheros y directorios de un directorio en concreto. Para ello necesitas una función existente en la librería os (Sistema Operativo) de Python.
- Recorre todos los resultados obtenidos por la función anterior. Lo puedes hacer, por ejemplo, con un bucle for.
- Imprime por pantalla solo aquellos resultados que sean ficheros (para ello también necesitas una función existente en os.
"""

# Solución 1, aplicando mi lógica y con prueba y error.
import humanize
import os

def ficheros(ruta):
    contenido = os.listdir(ruta)
    print("Aquí se muestran solamente ficheros \n" )
# hora utilizamos el bucle for.
    for archivo in contenido:
        if os.path.isfile(ruta+ '\\' +archivo):
            print(archivo)
# Ampliación: Lista el tamaño de los archivos en formato humano

    tamanyo = 0
    for filename in os.listdir(ruta):
        tamanyo = tamanyo + os.path.getsize(os.path.join(ruta, filename))
        print(tamanyo, (humanize.naturalsize(tamanyo)))

if __name__ == "__main__":
    ruta = input("Intruduce la ruta: \n")
    ficheros(ruta)

# Solución 2, leyendo la documentación oficial Python de la libreria os: https://docs.python.org/es/3/library/os.html

# import os (ya importado anteriormente, lo marco como anotación)

print("----------------------------------------------------------")

directorio_descargas = '/Users/Marquino/Downloads'
with os.scandir(directorio_descargas) as archivos:
    archivos = [archivos.name for archivos in archivos if archivos.is_file()]
    print(archivos)
