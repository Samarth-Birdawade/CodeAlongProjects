import socket
import logging

try:
    print("Socket Server is starting...")

    host = 'localhost'
    port = 6767

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind((host, port))
    s.listen(1)

    logging.info(f"Server listening on {host}:{port}")
    print("Waiting for connection...")

    client_socket, addr = s.accept()

    fileName = client_socket.recv(1024)
    
    with open(fileName, 'rb+') as f:
        while True:
            bytes_read = f.read(1024)
            if not bytes_read:
                break
            client_socket.sendall(bytes_read)
    print(f"Data sent to {addr}")

except Exception as e:
    logging.error(f"Socket error: {e}")
    print(f"Socket error: {e}")