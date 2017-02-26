"""
Sender module
"""
import threading
#import xbmc

class SenderThread(threading.Thread):
    """
    SenderThread class
    """
    status = ''

    def __init__(self, event, connection):
        threading.Thread.__init__(self)
        self.connection = connection
        self.event = event

    def run(self):
        while True:
            try:
                self.connection.sendall(SenderThread.status.encode())
                self.event.wait()
            except Exception as e:
                # Clean up the connection
                self.connection.close()
                xbmc.executebuiltin('Notification(Relay Addon Service, ERROR: '+e.message +',1000,//storage/.kodi/addons/service.relay.master/icon.png)')
                break
