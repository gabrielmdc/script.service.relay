#!/usr/bin/env python
import time
import xbmc
import socket
from clientSocket import ClientThread

 
if __name__ == '__main__':
    monitor = xbmc.Monitor()
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the port
    server_address = ('', 10000)
    sock.bind(server_address)
    # Listen for incoming connections
    sock.listen(1)

    while not monitor.abortRequested():
        # Wait for a connection
        connection, client_address = sock.accept()
        # xbmc.executebuiltin('Notification(Relay Addon Service, Conected with ' + client_address + ',1000,//storage/.kodi/addons/service.relay.master/icon.png)')
        newthread = ClientThread(connection)
        newthread.start()
