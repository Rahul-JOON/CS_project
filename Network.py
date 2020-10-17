import socket

class Net():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = '192.168.1.105'
        self.port = 5555
        self.addr = (self.server, self.port)
        self.answer = self.connect()

    def connect(self):
        try :
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            print("error in sending")
    
    def send(self, data):
        try :
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as s:
            print(s)

n = Net()
print(n.send("hehe"))                       