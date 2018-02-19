import socket

sock = socket.socket()
sock.bind(('', 1324))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr)

while True:
    data = conn.recv(1024)
    text = data.decode('utf-8')
    text = int(text) ** 2
    text = str(text)
    data = text.encode('utf-8')
    conn.send(data.upper())
conn.close()
