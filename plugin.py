import sys, re
import xbmc, xbmcplugin, xbmcgui

from resources.lib import Subsonic

base_url=sys.argv[0]
handle=int(sys.argv[1])

def addDir(name,url,mode,iconimage):
    if mode == None or url == None or len(url) < 1:
        fetchFolder()
    elif mode == 1:
        print(url)
    elif mode == 2:
        print(name + ":" + url)

def fetchFolder():
    subsonic = Subsonic.Subsonic('http://bruelldb:4040', 'test', 'test')
    folders = subsonic.getMusicFolders()
    total=len(folders)
    for folder in folders['musicFolders']['musicFolder']:
        addToXbmc("test", "test", 1, total)
        #addToXbmc(folder['name'], folder['name'], 1)

def handleFolder(folder):
    subsonic = Subsonic.Subsonic('http://bruelldb:4040', 'test', 'test')
    indexes = subsonic.getIndexes(folder['id'])['indexes']
    indexList = indexes['index']
    return indexList

def addToXbmc(name,link,mode,totalItems=0):
    xbmc.log('name: ' + str(name) + ", link: " + str(link) + ", mode: " + str(mode), xbmc.LOGNOTICE)
    title=decode(name)
    img=''
    #liz=xbmcgui.ListItem(title, iconImage="DefaultFolder.png")
    liz=xbmcgui.ListItem(title, iconImage=img, thumbnailImage=img)
    #liz.setInfo(type="music", infoLabels={"Title": title})
    url=base_url + "?folder=" + name
    xbmc.log('handle: ' + str(handle) + ", url: " + url, xbmc.LOGNOTICE)
    ok = xbmcplugin.addDirectoryItem(handle=handle, url=url, listitem=liz, isFolder=True, totalItems=totalItems)
    return ok

def _callback(matches):
    id = matches.group(1)
    try:
        return unichr(int(id))
    except:
        return id

def decode(data):
    if type(data) is int:
        data = unicode(data)
    return re.sub("&#(\d+)(;|(?=\s))", _callback, data).strip()

addDir(None,None,None,None)
