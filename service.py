"""
Main program
"""
import sys
import os
import xbmc
import xbmcaddon
from resources.gcrserver.main import Main


addon = xbmcaddon.Addon()
addonPath = addon.getAddonInfo("path")
databasePath = addonPath + addon.getSetting('SOCKET_PORT')

SOCKET_PORT = int(addon.getSetting('SOCKET_PORT'))
DB_FILE = databasePath


def main(m):
    """
    Main program
    """
    monitor = xbmc.Monitor()
    while not monitor.abortRequested():
        # Sleep/wait for abort for 10 seconds
        if monitor.waitForAbort(10):
            # Abort was requested while waiting. We should exit
            break
        m.listen_new_connection()


if __name__ == '__main__':
    m = Main(SOCKET_PORT, DB_FILE)
    try:
        main(m)
    except Exception as e:
        print('Bye!')
        xbmc.log('Logging Failure: %s' % (e.message), xbmc.LOGERROR)
    finally:
        m.close_socket_connection()