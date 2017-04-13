"""
Main program
"""
import socket
import threading
import sys
import xbmc
import os
import xbmcaddon
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/resources/lib")
from receiver import ReceiverThread
from supervisor import SupervisorThread
from connection import Connection

addon = xbmcaddon.Addon()
PORT = int(addon.getSetting('PORT'))
GPIO_PORT = int(addon.getSetting('GPIO_PORT'))
GPIO_PATH = addon.getSetting('GPIO_PATH')
GPIO_FILE_NAME = os.path.join(GPIO_PATH, 'gpio' + str(GPIO_PORT), 'value')

def set_up_gpio(gpio_port):
    """
    Prepare the gpio port to be used
    """
    addonPath = addon.getAddonInfo("path")
    scriptPath = os.path.join(addonPath, 'resources', 'lib', 'relay.sh')
    os.system("sh " + scriptPath + " " + str(gpio_port))
    #EXPORT_FILE = '/sys/class/gpio/export'
    #DIRECTION_FILE = '/sys/class/gpio/gpio'+str(gpio_port)+'/direction'

    #with open(EXPORT_FILE, 'w+') as f:
    #    f.write(str(gpio_port))
    #with open(DIRECTION_FILE) as ff:
    #    ff.write('out')

if __name__ == '__main__':
    monitor = xbmc.Monitor()

    event = threading.Event()
    ReceiverThread.FILE_NAME = GPIO_FILE_NAME
    supervisor = SupervisorThread(GPIO_FILE_NAME, event)

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the port
    server_address = ('', PORT)
    sock.bind(server_address)
    # Listen for incoming connections
    sock.listen(1)
    set_up_gpio(GPIO_PORT)
    supervisor.start()
    while not monitor.abortRequested():
        try:
            # Wait for a connection
            conn, client_address = sock.accept()
            connection = Connection(conn, (client_address[0], PORT), event)
            connection.start()
        except:
            break

    sock.close()
sys.exit(1)

