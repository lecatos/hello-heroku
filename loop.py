import socket, os
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 0))
s.sendto(b"@", ("103.28.243.130", 9000))
s.sendto(b"@", ("103.28.243.130", 17191))
while True:
  s.recvfrom(9999)
  s.sendto(b"@", ("103.28.243.130", 9000))
