#!/usr/bin/env python3
import os
import re
import sys

import daemon as Daemon


def main():
    daemon = False
    for arg in sys.argv:
        if re.match('-d', arg) or re.match('--daemon', arg):
            daemon = True
    if daemon:
        myDaemon = Daemon.Daemon(os.getpid())
        myDaemon.start()
    

if __name__ == '__main__':
    main()
