#!usr/bin/python
from thread import *
import socket
import sys

def clientthread(conn):
    buffer=""
    while True:
        data = conn.recv(8192)
        buffer+=data
        print buffer
    #conn.sendall(reply)
    conn.close()

def main():
    try:
        port = 6666
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        s.bind(('localhost', port))
        s.listen(10)
        print "[*] Server listening on localhost %d" %( port)

        conn, addr = s.accept()
        s.close()

    except KeyboardInterrupt as msg:
        sys.exit(0)


if __name__ == "__main__":
    main()
