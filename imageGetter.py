#!/usr/bin/env python3

import pathlib
import os
import requests

appDir = ''

def __init__():
    global appDir
    appDir = os.environ["HOME"] + '/.oshirase/thumbs/'
    if not appDirExists(appDir):
        createAppDir(appDir)

def appDirExists(path):
    return pathlib.Path(path).exists()
def createAppDir(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        print("Folder exists, doing nothing")

def downloadImage(username, url):
    imagePath = appDir+"%s.png" % username
    response = requests.get(url)
    file = open(imagePath, "wb")
    file.write(response.content)
    file.close()
    return imagePath

        
if __name__ == "imageGetter":
    __init__()
