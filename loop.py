import socket, os
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", os.environ["PORT"]))
while True:
  data, addr = s.recvfrom(1024)
  s.sendto(b"hello man", addr)
