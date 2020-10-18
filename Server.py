import sys
import socket
from _thread import *

server = '192.168.1.105'

port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try :
    s.bind((server, port))
except socket.error as e:
    str(e)

def client(conn):
    reply = ''
    while True:
        try :
            data = conn.recv(2048)
            reply = data.decode('utf-8')

            if not data:
                print("Disconnected")

            else :
                print("still connected Bro")
            
            conn.sendall(str.encode(reply))

        except:
            break
    conn.close()

while True: 

    s.listen()
    print("not connected")
    conn, addr = s.accept()
    print("connected to", coon, addr)

    start_new_thread(client, (conn, ))