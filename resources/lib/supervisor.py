"""
Module Supervisor
"""
import threading
from sender import SenderThread

class SupervisorThread(threading.Thread):
    """
    SupervisorThread class
    """
    def __init__(self, file_name, event):
        threading.Thread.__init__(self)
        self.file_name = file_name
        self.event = event

    def get_status(self):
        """
        get status method
        """
        with open(self.file_name) as f:
            return f.read(1)

    def run(self):
        while True:
            try:
                status_from_file = self.get_status()
                if status_from_file != "" and SenderThread.status != status_from_file:
                    SenderThread.status = status_from_file
                    self.event.set()
                    self.event.clear()
            except:
                self.event.set()
                self.event.clear()
                break
