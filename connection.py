"""
Connection module
"""
import socket
import threading
from receiver import ReceiverThread
from sender import SenderThread

class Connection(threading.Thread):
    """
    Connection class
    """
    def __init__(self, connection, address_port, event):
        threading.Thread.__init__(self)
        self.connection = connection
        self.address_port = address_port
        self.event = event

    def run(self):
        receiver = ReceiverThread(self.connection)
        sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sender_socket.connect(self.address_port)
        sender = SenderThread(self.event, sender_socket)

        receiver.start()
        sender.start()
