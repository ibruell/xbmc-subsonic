from resources.lib import Subsonic


s = Subsonic.Subsonic('http://bruelldb:4040', 'test', 'test')

def fetchMusicFolder():
    print(s.ping())
    print('=================')
    folders = s.getMusicFolders()
    for folder in folders['musicFolders']['musicFolder']:
        print(folder['name'])
        #handleFolder(folder)

def handleFolder(folder):
    indexes = s.getIndexes(folder['id'])['indexes']
    indexList = indexes['index']
    shortcuts = indexes.get('shortcut')
    childs = indexes.get('child')
    
    #print('indexes: ' + str(indexList))
    #print('Shortcuts: ' + str(shortcuts))
    #print('Childs: ' + str(childs))

    if isinstance(indexList, list):
        handleIndexesList(indexList)
    elif isinstance(indexList, dict):
        handleIndexes(indexList)

def handleIndexesList(indexesList):
    for indexes in indexesList:
        handleIndexes(indexes)

def handleIndexes(index):
    handleIndexArtists(index['artist'])

def handleDirectoryList(directoryList):
    for directory in directoryList:
        handleDirectory(directory)

def handleDirectory(directory):
    child = directory['child']
    if isinstance(child, list):
        handleDirChildList(child)
    elif isinstance(child, dict):
        handleDirChild(child)

def handleDirChildList(childList):
    for child in childList:
        handleDirChild(child)

def handleDirChild(child):
    if child['isDir'] == True:
        fetchMusicDir(child['id'])
    else:
        if isinstance(child, list):
            handleAlbumList(child)
        elif isinstance(child, dict):
            handleAlbum(child)

def fetchMusicDir(id):
    directory = s.getMusicDirectory(id)['directory']
    if isinstance(directory, list):
        handleDirectoryList(directory)
    elif isinstance(directory, dict):
        handleDirectory(directory)

def fetchArtists():
    artistsList = s.getArtists()
    indexes = artistsList.get('artists')
    for index in indexes.get('index'):
        print(' ')
        print(index['name'])
        
        handleIndexArtists(index['artists'])

        print('---------------')

def handleIndexArtists(artists):
        if isinstance(artists, list):
            handleArtistList(artists)
        elif isinstance(artists, dict):
            handleArtist(artists)

def handleArtistList(artistList):
    for artist in artistList:
        handleArtist(artist)

def handleArtist(artist):
    print(artist['name'])
    directory = fetchMusicDir(artist['id'])
    print(directory)
#    print(artist)
#    artistInfo = s.getArtist(artist['id'])
#    print(artistInfo)
#    if artistInfo:
#        album = artistInfo.get('artist').get('album')
#        if isinstance(album, dict):
#            handleAlbum(album)
#        elif isinstance(album, list):
#            handleAlbumList(album)

def handleAlbumList(albumList):
    for album in albumList:
        handleAlbum(album)

def handleAlbum(album):
    print('  ' + album['album'] + ' - ' + album['title'])

fetchMusicFolder()
#fetchVideoFolder()
#fetchArtists()
