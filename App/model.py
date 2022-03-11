"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from datetime import date
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'albums': None,
               'artists': None,
               'tracks': None}

    catalog['albums'] = lt.newList(datastructure='ARRAY_LIST')
    catalog['artists'] = lt.newList(datastructure='SINGLE_LINKED', cmpfunction=compareartists)
    catalog['tracks'] = lt.newList(datastructure='SINGLE_LINKED', cmpfunction=comparetrackname)

    return catalog

# Funciones para agregar informacion al catalogo

def addAlbum(catalog, album):
    """
    Adiciona un track a la lista de tracks
    """
    a = newAlbum(album['name'],album['id'], album['release_date'])
    lt.addLast(catalog['albums'], a)
    return catalog


def addArtist(catalog, artist):
    """
    Adiciona un track a la lista de tracks
    """
    at = newTrack(artist['name'], artist['id'])
    lt.addLast(catalog['artists'], at)
    return catalog


def addTrack(catalog, track):
    """
    Adiciona un track a la lista de tracks
    """
    t = newTrack(track['name'], track['id'])
    lt.addLast(catalog['tracks'], t)
    return catalog
    
def newArtist(name):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    artist = {'name': "", "Albums": None,  "average_rating": 0}
    artist['name'] = name
    artist['Albums'] = lt.newList('ARRAY_LIST')
    return artist

def newTrack(name, id):
    """
    Esta estructura almancena los tracks utilizados para marcar libros.
    """
    track = {'name': '', 'id': '' }
    track['name'] = name
    track['id'] = id
    return track

def newAlbum(name, id, date):
    album = {'name': '', 'id': '', 'release_date': ''}
    album['id']= id
    album['name']= name
    album['release_date']= date
    return album
    
def getLastThreeAlbums(catalog):
    
    """
    Retorna los mejores libros
    """
    tamanhoAlbum = albumSize(catalog)
    albums = catalog['albums']
    lastThreeAlbums = lt.newList()
    for cont in range(tamanhoAlbum-2, tamanhoAlbum+1):
        album = lt.getElement(albums, cont)
        lt.addLast(lastThreeAlbums, album)
    
    return lastThreeAlbums

def getLastThreeArtists(catalog):
    
    """
    Retorna los mejores libros
    """
    tamanhoArtist = artistsSize(catalog)
    artists = catalog['artists']
    lastThreeArtists = lt.newList()
    for cont in range(tamanhoArtist-2, tamanhoArtist+1):
        artist = lt.getElement(artists, cont)
        lt.addLast(lastThreeArtists, artist)
    
    return lastThreeArtists 

def getLastThreeTracks(catalog):
    
    """
    Retorna los mejores libros
    """
    tamanhoTracks = tracksSize(catalog)
    tracks = catalog['tracks']
    lastThreeTracks = lt.newList()
    for cont in range(tamanhoTracks-2, tamanhoTracks+1):
        track = lt.getElement(tracks, cont)
        lt.addLast(lastThreeTracks, track)
    
    return lastThreeTracks 

def getAlbumsRange(catalog, fechaI, fechaF):
    
    albums = catalog['albums']['elements']
    merge_sort_result  = merge_sort(albums)
    ret = []
    for i in range(len(merge_sort_result)):
        if merge_sort_result[i]['release_date'] >= fechaI and merge_sort_result[i]['release_date'] <= fechaF:
            ret.append(merge_sort_result[i])
        else:
            continue
    return ret
    

# Funciones utilizadas para comparar elementos dentro de una lista
def compareartists(artistname1, artist):
    if artistname1.lower() == artist['name'].lower():
        return 0
    elif artistname1.lower() > artist['name'].lower():
        return 1
    return -1


def comparetrackname(name, track):
    if (name == track['name']):
        return 0
    elif (name > track['name']):
        return 1
    return -1

def compareratings(album1, album2):
    return (str(album1['name']) > str(album2['name']))
# funciones para comparar elementos dentro de algoritmos de ordenamientos
def sortAlbums(catalog):
    sa.sort(catalog['albums'], compareratings)
# Funciones de ordenamiento

def merge_sort(lista):
    if len(lista) < 2:
        return lista
    else:
        medio = len(lista)//2
        derecha = merge_sort(lista[:medio])
        izquierda = merge_sort(lista[medio:])
        return merge(derecha, izquierda)
    
def merge(lista1, lista2):
    i,j = 0, 0
    resultado = []
    while(i<len(lista1) and j <len(lista2)):
        if(lista1[i]['release_date']<lista2[j]['release_date']):
            resultado.append(lista1[i])
            i+=1
        else: 
            resultado.append(lista2[j])
            j+=1
    resultado += lista1[i:]
    resultado += lista2[j:]
    return resultado


# Funciones de consulta

def albumSize(catalog):
    return lt.size(catalog['albums'])


def artistsSize(catalog):
    return lt.size(catalog['artists'])


def tracksSize(catalog):
    return lt.size(catalog['tracks'])