import socket
import time
from pythonosc import osc_message_builder
from pythonosc import udp_client

host = ''
port = 8888
bufsiz = 128
addr = (host,port)

udpSerSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSerSock.bind(addr)

print("osc messages are sending to port 8086")
while True:
	data,addr = udpSerSock.recvfrom(bufsiz)
	value = data.split(b".")
	client = udp_client.UDPClient("localhost", 9999)
	for i in range(len(value)):
		if len(value[i]) ==  27:
			value[i] = value[i].split(b",")
			osclist = [int(field) for field in value[i][1:]]
#			print(osclist)
			msg = osc_message_builder.OscMessageBuilder(address = "/YYSeesaw")
			for n in range(5):
			  msg.add_arg(osclist[n])
			msg = msg.build()
			client.send(msg)
	time.sleep(0.1)
