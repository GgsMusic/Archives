import socket
import time
from struct import unpack

port = 8888
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",port))
print('waiting on port:', port)
while True:
	data, addr = s.recvfrom(12)
	data = unpack("2s5h", data)
	print("Data:", data, "From:", addr)
	time.sleep(1)
