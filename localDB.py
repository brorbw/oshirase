#!/usr/bin/env python3

import os
import json
import pathlib
import sys

data = []

appDir = ''
databaseName = ''

def __init__():
    global appDir
    appDir = os.environ["HOME"] + '/.oshirase/'
    global databaseName
    databaseName = 'db.json'
    global data
    data = loadDB(appDir, databaseName)

def loadDB(_appDir, databaseName):
    data = []
    if not appDirExists(_appDir):
        createAppDir(_appDir)
    try:
        data = readFile(_appDir + databaseName)
    except json.decoder.JSONDecodeError:
        print('Database is currupted. This is not serious!\nLet us create a new one')
        writeFile(_appDir + databaseName, '[]')
        print('DONE!')
    except FileNotFoundError:
        print('DB empty or not found\nCreating it...')
        writeFile(_appDir + databaseName, '[]')
        print('DONE!')
    except PermissionError:
        print('It appears that you don\'t have permissions to your HOME\nThat\'s just silly')
    except:
        print('¯\_(ツ)_/¯')
    finally:
        return data
    
def readFile(path):
    content = ''
    with open(path) as json_file:
        content = json.load(json_file)
        json_file.close
    return content

def writeFile(path, data):
    with open(path, 'w') as outfile:
        outfile.write(data)
        outfile.close
    
def getLatestContent(username):
    for user in data:
        if user['name'] == username:
            return user
    raise UsernameNotFound("Username %s not found" % username)

def appDirExists(path):
    return pathlib.Path(path).exists()

def createAppDir(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        print("Folder exists, doing nothing")
    

def setLatestContent(username, hash):
    for user in data:
        if user['name'] == username:
            user['hash'] = hash
            with open(appDir + databaseName, 'w') as outfile:
                json.dump(data, outfile)
                outfile.close
            return
    raise UsernameNotFound("Username %s not found" % username)

def createLatestContent(username, hash):
    user = {
        "name": username,
        "hash": hash
    }
    data.append(user)
    with open(appDir + databaseName, 'w') as outfile:
        json.dump(data, outfile)
        outfile.close

class UsernameNotFound(Exception):
    pass

if __name__ == 'localDB':
    __init__()

