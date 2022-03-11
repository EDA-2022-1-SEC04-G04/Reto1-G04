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
 """

from App.model import sortAlbums
import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""
def newController():
    """
    Crea una instancia del modelo
    """
    control = {
        'model': None
    }
    control['model'] = model.newCatalog()
    return control
# Inicialización del Catálogo de libros

def loadData(control):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    catalog = control['model']
    albums = loadAlbums(catalog)
    tracks = loadTracks(catalog)
    artists = loadArtists(catalog)
    sortAlbums(catalog)
    return albums, artists, tracks

def getLastThreeAlbums(control):
    """
    Retorna los mejores libros
    """
    lastThreeAlbums = model.getLastThreeAlbums(control['model'])
    return lastThreeAlbums

def getLastThreeArtists(control):
    """
    Retorna los mejores libros
    """
    lastThreeArtists = model.getLastThreeArtists(control['model'])
    return lastThreeArtists

def getLastThreeTracks(control):
    """
    Retorna los mejores libros
    """
    lastThreeTracks = model.getLastThreeTracks(control['model'])
    return lastThreeTracks   

def getAlbumsRange(control, fechaI, fechaF):
    albums = model.getAlbumsRange(control['model'], fechaI, fechaF)
    print(albums)
    return albums

def loadAlbums(catalog):
    """
    Carga los albumes del archivo.  Por cada album se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al album que se esta procesando.
    """
    albumsFile = cf.data_dir + 'spotify-albums-utf8-small.csv'
    input_file = csv.DictReader(open(albumsFile, encoding='utf-8'))
    for album in input_file:
        model.addAlbum(catalog, album)
    return model.albumSize(catalog)


def loadTracks(catalog):
    """
    Carga todos los tags del archivo y los agrega a la lista de tags
    """
    tracksfile = cf.data_dir + 'spotify-tracks-utf8-small.csv'
    input_file = csv.DictReader(open(tracksfile, encoding='utf-8'))
    for track in input_file:
        model.addTrack(catalog, track)
    return model.tracksSize(catalog)


def loadArtists(catalog):
    """
    Carga la información que asocia tags con libros.
    """
    artistsfile = cf.data_dir + 'spotify-artists-utf8-small.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)
    return model.artistsSize(catalog)



# Funciones para la carga de datos
def sortBooks(catalog):
    """
    Ordena los libros por average_rating
    """
    model.sortAlbums(catalog)
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
