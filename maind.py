import biblioteca

lista_canciones = []
lista_canciones = biblioteca.cargar_lista("playlist.txt")
print(biblioteca.buscar_cancion(lista_canciones, "Yesterday"))