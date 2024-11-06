# cargar canciones
import biblioteca

lista_canciones = []

lista_canciones = biblioteca.cargar_lista("playlist.txt")
#print(lista_canciones)

# guardar cancion

biblioteca.agregar_cancion(lista_canciones, "Europa VII", "La Oreja de Van Gogh","Pop")
#print(lista_canciones)

#eliminar cancion

biblioteca.eliminar_cancion(lista_canciones,"Europa VII")
print(lista_canciones)

#contar

#print(biblioteca.contar_canciones(lista_canciones))

#buscar por artista

biblioteca.agregar_cancion(lista_canciones, "Innuendo", "Queen", "Rock")
#print(biblioteca.buscar_por_artista(lista_canciones, "Queen"))

#guardar lista

lista_canciones2 = [
    {
    "Nombre": "La Reina del Pop",
    "Artista": "La Oreja de Van Gogh",
    "Genero": "Pop"
    },
    {
    "Nombre": "Lasai Lasai",
    "Artista": "Huntza",
    "Genero": "Folk"
    },
    {
    "Nombre": "Aldapan Gora",
    "Artista": "Huntza",
    "Genero": "Folk"
    },
    {
    "Nombre": "Dancing in a Hurricane",
    "Artista": "Epica",
    "Genero": "Metal sinfonico"
    }
]

#biblioteca.guardar_lista(lista_canciones2, "miplaylist.txt")

#buscar_cancion
print(biblioteca.buscar_cancion(lista_canciones, "Yesterday"))