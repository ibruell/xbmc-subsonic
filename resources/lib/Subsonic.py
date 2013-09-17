import JsonHelper

class Subsonic:
    serverParams = {'apiVersion': '1.8.0',
                    'clientName': 'XBMC Plugin'}
    helper = JsonHelper.JsonHelper()

    def __init__(self, server, user, password):
        self.serverParams.update({'server': server,
                            'user':  user,
                            'password': password})

    def ping(self):
        return self.__callMethod("ping.view")

    def getArtists(self):
        return self.__callMethod("getArtists.view")

    def getArtist(self, artistId):
        return self.__callMethod("getArtist.view", {'id': artistId})

    def getIndexes(self, folderId):
        return self.__callMethod("getIndexes.view", {'musicFolderId': folderId})

    def getMusicFolders(self):
        return self.__callMethod("getMusicFolders.view")

    def getMusicDirectory(self, folderId):
        return self.__callMethod("getMusicDirectory.view", {'id': folderId})

    def __callMethod(self, method, queries={}):
        return self.helper.callMethod(self.serverParams, method, queries)

