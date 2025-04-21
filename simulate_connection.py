import socketio
import time

# Create a Socket.IO client instance
sio = socketio.Client()

# Event to handle connection
@sio.event
def connect():
    print("Successfully connected to the server.")

# Event to handle disconnection
@sio.event
def disconnect():
    print("Disconnected from the server.")

# Connect to the Flask server (ensure Flask is running)
sio.connect('http://127.0.0.1:5000')  # Ensure Flask is running

# Function to simulate a connection attempt and log it
def simulate_connection():
    log_data = {
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
        'event_type': 'Connection',
        'ip_address': '192.168.0.1',
        'message': 'Attempted SSH login'
    }
    
    # Emit the log to the Flask backend via Socket.IO after confirming connection
    if sio.connected:
        sio.emit('new_log', log_data)
        print(f"Simulated Log: {log_data}")
    else:
        print("Not connected to the server. Retrying...")

# Simulate connections at regular intervals
if __name__ == '__main__':
    try:
        while True:
            simulate_connection()
            time.sleep(2)  # Simulate every 2 seconds
    except KeyboardInterrupt:
        print("Simulation stopped.")
        sio.disconnect()
