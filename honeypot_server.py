import socket
import logging

HOST = '0.0.0.0'
PORT = 9999

# Configure logging
logging.basicConfig(filename='honeypot.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Start honeypot server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[+] Honeypot listening on port {PORT}...")
    
    while True:
        client_socket, client_address = server.accept()
        with client_socket:
            print(f"[!] Connection from {client_address}")
            logging.info(f"Connection from {client_address}")
            client_socket.sendall(b"Fake service: Access Denied.\n")
