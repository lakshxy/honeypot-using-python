import socket

HOST = 'localhost'  # The server's hostname or IP address
PORT = 5000         # The port used by your Flask honeypot server (make sure it's the same as your Flask app's port)

# Create a socket connection
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # Connect to the honeypot (Flask server)
    s.sendall(b'Hello, honeypot!')  # Send a message to the server
    data = s.recv(1024)  # Receive a response from the server

print('Received', repr(data))  # Print the response
