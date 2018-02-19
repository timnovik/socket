import socket
import random
sock = socket.socket()
sock.connect(('localhost', 1324))
while True:
    text = str(random.randint(1,400))
    data = text.encode('utf-8')
    sock.send(data)
    data = sock.recv(1024)
    data = data.decode('utf-8')
    print(text)
    print(data)
sock.close()

