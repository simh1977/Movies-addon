#   Copyright (C) 2017 Lunatixz
#
#
# This file is part of filmriseTV.
#
# filmriseTV is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# filmriseTV is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with filmriseTV.  If not, see <http://www.gnu.org/licenses/>.

# -*- coding: utf-8 -*-

import os, sys
import xbmc, xbmcaddon, xbmcgui, xbmcplugin

# Plugin Info
ADDON_ID = 'plugin.video.bestmovies'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME = REAL_SETTINGS.getAddonInfo('name')
ADDON_PATH = (REAL_SETTINGS.getAddonInfo('path').decode('utf-8'))
ADDON_VERSION = REAL_SETTINGS.getAddonInfo('version')
SETTINGS_LOC = REAL_SETTINGS.getAddonInfo('profile')
ICON = REAL_SETTINGS.getAddonInfo('icon')
FANART = REAL_SETTINGS.getAddonInfo('fanart')

def start():
    addDir(
        title="Recherche",
        url="plugin://plugin.video.youtube/search/?q=/")
    addDir(
        title="movies",
        url="plugin://plugin.video.youtube/search/?q=movies+2020+full+movie&app=desktop/")
    addDir(
        title="Film haitien",
        url="plugin://plugin.video.youtube/search/?q=film+haitien+complet/")
    addDir(
        title="Film Africain Fr",
        url="plugin://plugin.video.youtube/search/?q=film+africain+complet+en+francais/")
    addDir(
        title="Konpa Live",
        url="plugin://plugin.video.youtube/search/?q=konpa+live+complet/")
    addDir(
        title="Jazz Concert",
        url="plugin://plugin.video.youtube/search/?q=jazz+concert/")

      
def addDir(title, url):
    liz=xbmcgui.ListItem(title)
    liz.setProperty('IsPlayable', 'false')
    liz.setInfo(type="Video", infoLabels={"label":title,"title":title} )
    liz.setArt({'thumb':ICON,'fanart':FANART})
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)
    
start()
xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=True)