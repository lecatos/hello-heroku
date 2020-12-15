import socket, os ,sys
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", str(sys.argv[1])))
s.sendto(b"@PORT: "+ str(s.getsockname()[1]).encode(), ("103.28.243.130", 9000))
s.sendto(b"@", ("103.28.243.130", 17192))
while True:
  d, addr  = s.recvfrom(9999)
  s.sendto(d + b"@PORT: "+ str(s.getsockname()[1]).encode(), ("103.28.243.130", 9000))
