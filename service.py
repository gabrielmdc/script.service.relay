"""
Main program
"""
import socket
import threading
import sys
import xbmc
import os
from receiver import ReceiverThread
from supervisor import SupervisorThread
from connection import Connection

PORT = 10001
GPIOPORT = 18
FILE_NAME = '/sys/class/gpio/gpio' + str(GPIOPORT) + '/value'

def set_up_gpio(gpio_port):
    """
    Prepare the gpio port to be used
    """
    os.system("sh /storage/.kodi/addons/service.relay.master/relay.sh " + str(GPIOPORT))
    #EXPORT_FILE = '/sys/class/gpio/export'
    #DIRECTION_FILE = '/sys/class/gpio/gpio'+str(gpio_port)+'/direction'

    #with open(EXPORT_FILE, 'w+') as f:
    #    f.write(str(gpio_port))
    #with open(DIRECTION_FILE) as ff:
    #    ff.write('out')

if __name__ == '__main__':
    monitor = xbmc.Monitor()

    event = threading.Event()
    ReceiverThread.FILE_NAME = FILE_NAME
    supervisor = SupervisorThread(FILE_NAME, event)

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the port
    server_address = ('', PORT)
    sock.bind(server_address)
    # Listen for incoming connections
    sock.listen(1)

    supervisor.start()
    set_up_gpio(GPIOPORT)
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

