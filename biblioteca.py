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



def agregar_cancion(lista_canciones, nombre, artista, genero):
    if buscar_cancion(lista_canciones, nombre) == -1: 
        cancion = {
        "Nombre": nombre,
        "Artista": artista,
        "Genero": genero
        }
        lista_canciones.append(cancion)
        print("Cancion agregada con exito")


def eliminar_cancion(lista_canciones, nombre):
    del lista_canciones[buscar_cancion(lista_canciones, nombre)]


def buscar_cancion(lista_canciones, nombre):
    for i,cancion in enumerate (lista_canciones):
        if nombre in cancion["Nombre"]:
            break
        else:
            i = -1
    return i

#buscar enumerate
#for i,cancion in enumerate(lista_canciones) ahora devuelve la posicion en vez del buleano



def contar_canciones(lista_canciones):
    return len(lista_canciones)



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


def crear_lista_aleatoria(canciones, n):
    lista_aleatoria = []

    if n <= len(canciones):
        lista_aleatoria = random.sample(list(canciones.keys()), n)

    return lista_aleatoria

#print(crear_lista_aleatoria(dictCanciones, 3))


def guardar_lista(lista_canciones, nombre_fichero):
    with open(nombre_fichero, "w") as fichero:
        for cancion in lista_canciones:
            fichero.write(f"{cancion["Nombre"]} - {cancion["Artista"]} - {cancion["Genero"]}\n")
