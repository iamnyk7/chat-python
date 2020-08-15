import socket
import  datetime

host='localhost'
port=6969
max_size=1024

print(f"starting client at {datetime.datetime.now()}")

c=socket.socket()
c.connect((host,port))

while True:
    msg=input()
    msg_encoded=msg.encode('utf-8')
    c.send(msg_encoded)
    if msg=='exit':
        break
    reply=c.recv(max_size).decode('utf-8')
    if reply=='exit':
        break
    print(f"At {datetime.datetime.now()} \n{host}:{port} said {reply}")
print(f"Closing server at {datetime.datetime.now()}")
c.close()