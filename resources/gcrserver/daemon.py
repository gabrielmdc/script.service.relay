#!/usr/bin/env python
import sys
from main import Main
from .pydaemon import PyDaemon

SOCKET_PORT = 10000
DB_FILE = "resources/database.db"


class Daemon(PyDaemon):

    def run(self):
        m = Main(SOCKET_PORT, DB_FILE)
        try:
            while True:
                m.listen_new_connection()
        except Exception as e:
            sys.stderr.write(str(e))
        finally:
            m.close_socket_connection()
            sys.exit(1)

    def stop(self):
        super().stop()


if __name__ == "__main__":
    daemon = Daemon("/tmp/gcr-server.pid")
    if len(sys.argv) > 1:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print("Usage: %s start|stop|restart|" % sys.argv[0])
sys.exit(2)
