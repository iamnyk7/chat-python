import socket
import datetime

host='localhost'
port=6969
max_size=1024

s=socket.socket()
s.bind((host,port))
print(f"Starting server at {datetime.datetime.now()}")

s.listen(5)

c,addr=s.accept()

while True:
    msg=c.recv(max_size).decode('utf-8')
    if msg=='exit':
        break
    print(f"At {datetime.datetime.now()} \n{addr} said {msg}")
    reply=input()
    reply_encoded=reply.encode('utf-8')
    c.send(reply_encoded)
    if reply=='exit':
        break
print(f"Closing server at {datetime.datetime.now()}")
c.close()
s.close()