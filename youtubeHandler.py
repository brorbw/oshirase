#!/usr/bin/env python3

import requests
import json
from bs4 import BeautifulSoup
import imageGetter

def buildYoutubeVideosURL(username):
    return 'https://www.youtube.com/c/%s/videos' % username

def getLatestVideoInfo(username):
    site = requests.get(buildYoutubeVideosURL(username))
    parsedSite = parseSite(site)
    recentVideoJSON = getMostRecentVideo(parsedSite)
    cleanYTJson = ytJSONToCleanJSON(username, recentVideoJSON)
    return cleanYTJson 
    
   
def getMostRecentVideo(blob):
    scripts = blob.find_all('script')
    ytInitialData = str(scripts[27])
    jsonString = ytInitialData[39:len(ytInitialData)- 119]
    return json.loads(jsonString)['contents']['twoColumnBrowseResultsRenderer']['tabs'][1]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['gridRenderer']['items'][0]['gridVideoRenderer']
    
    
def parseSite(site):
    return BeautifulSoup(site.content, 'html.parser')

def ytJSONToCleanJSON(username, videoItemJson):
    thumbPath = imageGetter.downloadImage(
        username,
        videoItemJson['thumbnail']['thumbnails'][0]['url'])
    return {
        "title": videoItemJson['title']['runs'][0]['text'],
        "videoId": videoItemJson['videoId'],
        "timeSinceRelease": videoItemJson['publishedTimeText']['simpleText'],
        "thumbnail": thumbPath,
        "link": "https://youtube.com%s" % videoItemJson['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url'],
    } 
