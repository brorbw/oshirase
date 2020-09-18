#!/usr/bin/env python3
import webbrowser
import gi
gi.require_version("Notify", "0.7")
from gi.repository import Notify, GdkPixbuf

def __init__():
    Notify.init('oshirase')

def showNotification(title, message, image, url):
    notification = Notify.Notification.new(
        title,
        message,
        image
    )
    notification.add_action(
        "action_click",
        "Open",
        lambda : openInBrowser(url)
    )
    notification.set_urgency(2)
    notification.show()
    
def openInBrowser(url):
    #TODO: get notification to open url
    webbrowser.open(url)

    
    
    Notify.uninit()
if __name__ == "notification":
    __init__()
