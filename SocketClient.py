import socket
import logging

try:
    print("Socket Client is starting...")
    s = socket.socket()
    
    host = 'localhost'
    port = 6767
    fileName = b'Data.txt'

    print("Connecting to server...")

    s.connect((host, port))
    s.sendall(fileName)

    content_received = s.recv(1024)

    print("Data received from server:")
    print(content_received.decode())

    s.close()

except Exception as e:
    logging.error(f"Socket error: {e}")
    print(f"Socket error: {e}")