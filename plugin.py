import xbmcplugin
import xbmcgui

import subsonic

def CATEGORIES():
    addDir("","",1,"")
    addDir("","",1,"")
    addDir("","",1,"")
    addDir("","",1,"")

def addDir(name,url,mode,iconimage):
    if mode == None or url == None or len(url) < 1:
        fetchFolder()
    elif mode == 1:
        print(url)
    elif mode == 2:
        print(name + ":" + url)

def fetchFolder():
    s = subsonic.Subsonic('http://bruelldb:4040', 'test', 'test')
    folders = s.getMusicFolders()
    for folder in folders['musicFolders']['musicFolder']:
        handleFolder(folder)

def handleFolder(folder):
    indexes = s.getIndexes(folder['id'])['indexes']
    indexList = indexes['index']
    return indexList

def addToXbmc(name,link,mode,iconimage):
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png")
    liz.setInfo(type="music", infoLabels={"Title": name})
    ok = xbmcplugin.addDirectory(handle=int(sys.argv[1]), url=link, listitem=liz, isFolder=True)
    return ok


CATEGORIES()
