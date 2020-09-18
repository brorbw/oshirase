#!/usr/bin/env python3
import os
import re

import localDB
import notification
import youtubeHandler


def runTask():
    userPath = os.environ["HOME"] + '/.oshiraserc'  
    youtube = readLines(userPath)
    for youtuber in youtube:
        print(youtuber)
        checkLatestVideo(youtuber)
    
    
def readLines(urlFilePath):
    try:
        file = open(urlFilePath, 'r')
        lines = file.readlines()
        arr = []
        for line in lines:
            if(re.match('^#', line)):
                continue
            arr.append(line.rstrip())
        return arr
    except FileNotFoundError:
        print('%s is not found. Please create it')

def checkLatestVideo(username):

    videoInfo = youtubeHandler.getLatestVideoInfo(username)
    
    recentVideoHash = hash(videoInfo['videoId']) 
    try:
        latestContent = localDB.getLatestContent(username)
    except localDB.UsernameNotFound:
        print("Username %s not found in DB\nCreating it" % username)
        localDB.createLatestContent(username, recentVideoHash)
        return
        
    if latestContent['hash'] == recentVideoHash:
        return False
    else:
        notification.showNotification(
            username,
            videoInfo['title'],
            videoInfo['thumbnail'],
            videoInfo['link']
            )
        localDB.setLatestContent(username, recentVideoHash)
