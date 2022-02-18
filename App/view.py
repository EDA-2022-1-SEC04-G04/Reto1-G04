"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (art your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def newController():
    """
    Se crea una instancia del controlador
    """
    control = controller.newController()
    return control

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2 - Mostrar información de los últimos 3 elementos de c/u")
    print("0- Salir del programa")

def loadData():
    """
    Solicita al controlador que cargue los datos en el modelo
    """
    albums, artists, tracks = controller.loadData(control)
    return albums, artists, tracks

def printInfoAlbum(album):
    """
    Imprime los mejores libros solicitados
    """
    size = lt.size(album)
    if size:
        print(' Esta es la información de los últimos 3 álbumes: ')
        for album in lt.iterator(album):
            print('Titulo del álbum: ' + album['name'])

def printInfoArtista(artist):
    """
    Imprime los mejores libros solicitados
    """
    size = lt.size(artist)
    if size:
        print('Esta es la información de los últimos 3 artistas: ')
        for artist in lt.iterator(artist):
            print('Nombre: ' + artist['name'])

def printInfoTrack(track):
    """
    Imprime los mejores libros solicitados
    """
    size = lt.size(track)
    if size:
        print('Esta es la información de las últimas 3 canciones: ')
        for track in lt.iterator(track):
            print('Nombre de la canción: ' + track['name'])

def printTest():
    print("Esto es una prueba")  

control = newController()
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        ab, art, tr = loadData()
        print('Álbumes cargados: ' + str(ab))
        print('Artistas cargados: ' + str(art))
        print('Tracks cargados: ' + str(tr))

    elif int(inputs[0]) == 2:
        
        album = controller.getLastThreeAlbums(control)
        printInfoAlbum(album)
        artista = controller.getLastThreeArtists(control)
        printInfoArtista(artista)
        track = controller.getLastThreeTracks(control)
        printInfoTrack(track)
        

    elif int(inputs[0]) == 0:
        sys.exit(0)

    else:
        continue
sys.exit(0)
