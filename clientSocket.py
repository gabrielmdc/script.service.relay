import os
import threading
import time

GPIOPORT = 18
fileName = '/sys/class/gpio/gpio' + str(GPIOPORT) + '/value'

def getStatus():
    with open(fileName) as f:
        return f.read(1)
        
class ClientThread(threading.Thread):

    def __init__(self, connection):
        threading.Thread.__init__(self)
        self.connection = connection
        
    def run(self):
        while(True):
            try:
                # Receive the data in small chunks and retransmit it
                data = self.connection.recv(10)
                # Protocol: MSG:INFO|ON|OFF
                if data:
                    action = data.split(':')
                    if(len(action) > 1):
                        if(action[1] == 'INFO'):
                            status = getStatus()
                            self.connection.sendall(status.encode())
                        elif(action[1] == 'ON' or action[1] == 'OFF'):
                            os.system("sh /storage/.kodi/addons/service.relay.master/relay.sh")
                            status = getStatus()
                            self.connection.sendall(status.encode())
                else:
                    self.connection.close()
                    break;
                
            except Exception as e:
                # Clean up the connection
                self.connection.close()
                xbmc.executebuiltin('Notification(Relay Addon Service, ERROR: '+e.message +',1000,//storage/.kodi/addons/service.relay.master/icon.png)')
                break;
