import random

# toma el nombre de un archivo de texto como argumento y devuelve una lista de diccionarios cancion.
def cargar_lista(fichero):#
    lista_canciones = []
    with open(fichero, "r") as fichero:
        for linea in fichero:
            nombre, artista, genero = linea.strip().split(" - ")
            cancion = {
                "Nombre": nombre,
                "Artista": artista,
                "Genero": genero
            }
            lista_canciones.append(cancion)
    
    return lista_canciones


# 1.2. Agregar Canción a Lista de Música:

def agregar_cancion(lista_canciones, nombre, artista, genero):
    cancion = {
    "Nombre": nombre,
    "Artista": artista,
    "Genero": genero
    }
    lista_canciones.append(cancion)


# # 1.3. Eliminar Canción de Lista de Música

def eliminar_cancion(lista_canciones, nombre):

    for cancion in lista_canciones:
        if nombre in cancion["Nombre"]:
            lista_canciones.remove(cancion)
            print(nombre + " se ha eliminado con exito")
            break


# # 2.1. Contar Canciones en una Lista

def contar_canciones(lista_canciones):
    return len(lista_canciones)




# # 2.2. Buscar Canciones por Artista: (2 puntos) Escribe una función llamada buscar_por_artista que tome un
# # diccionario de canciones y el nombre de un artista como argumentos, y devuelva una lista de todas las canciones
# # de ese artista.

def buscar_por_artista(lista_canciones, artista):
    lista_canciones_artista = []

    for cancion in lista_canciones:
        if cancion["Artista"] == artista:
            lista_canciones_artista.append(cancion)

    return lista_canciones_artista



"""
# # 2.3. Ordenar Lista de Música Alfabéticamente: (1 punto) Escribe una función llamada ordenar_alfabeticamente
# # que tome un diccionario de canciones como argumento y devuelva una lista de tuplas ordenadas alfabéticamente
# # por título de canción.

def ordenar_alfabeticamente(canciones):
    return sorted(canciones.items())
"""


# Parte 3: Creación de Listas de Reproducción

# # 3.1. Crear Lista de Reproducción Aleatoria: (2 puntos) Escribe una función llamada crear_lista_aleatoria que
# # tome un diccionario de canciones y un número n como argumentos, y devuelva una lista aleatoria de n canciones
# # del diccionario de canciones original.

def crear_lista_aleatoria(canciones, n):
    lista_aleatoria = []

    if n <= len(canciones):
        lista_aleatoria = random.sample(list(canciones.keys()), n)

    return lista_aleatoria

print(crear_lista_aleatoria(dictCanciones, 3))



# # 3.2. Guardar Lista de Reproducción en Archivo: 


def guardar_lista(lista_canciones, nombre_fichero):
    with open(nombre_fichero, "w") as fichero:
        for cancion in lista_canciones:
            fichero.write(f"{cancion["Nombre"]} - {cancion["Artista"]} - {cancion["Genero"]}\n")
