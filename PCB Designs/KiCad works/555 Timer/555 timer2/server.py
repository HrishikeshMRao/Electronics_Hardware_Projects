import  socket 
s=socket.socket
port = 12345
s.connect(('127.20.10.5' ,port))

print(s.recv(1024).decode())

s.close