"""
Receiver module
"""
import threading

class ReceiverThread(threading.Thread):
    """
    ReceiverThread class
    """
    FILE_NAME = ''

    def __init__(self, connection):
        threading.Thread.__init__(self)
        self.connection = connection

    @staticmethod
    def set_status(status):
        """
        set status
        """
        with open(ReceiverThread.FILE_NAME, "w") as f:
            f.write(status)

    @staticmethod
    def get_status_from_data(data):
        """
        get status from data
        """
        status = ''
        action = data.split(':')
        if len(action) > 1:
            if action[1] == 'ON':
                status = '1'
            elif action[1] == 'OFF':
                status = '0'
        return status

    def run(self):
        while True:
            # Receive the data in small chunks and retransmit it
            data = self.connection.recv(9)
            # Protocol: MSG:INFO|ON|OFF
            if data and data != 'END':
                status = ReceiverThread.get_status_from_data(data)
                if status != '':
                    ReceiverThread.set_status(status)
            else:
                self.connection.close()
                break
