from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import logging
from datetime import datetime

# Create Flask app and SocketIO object
app = Flask(__name__)
socketio = SocketIO(app)

# Set up logging to store events
logging.basicConfig(filename='honeypot.log', level=logging.INFO)

# Function to log events
def log_event(event_type, ip_address, message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = f"{timestamp} | {event_type} | {ip_address} | {message}"
    logging.info(log_message)
    
    # Emit log to frontend
    socketio.emit('new_log', {'timestamp': timestamp, 'event_type': event_type, 'ip_address': ip_address, 'message': message})

# Simulate a connection event and log it
@app.route('/simulate_connection')
def simulate_connection():
    log_event('Connection', '192.168.0.1', 'Attempted SSH login')
    return 'Connection simulated'

@app.route('/simulate_connection')
def simulate_connection():
    log_event('Connection', '192.168.0.1', 'Attempted SSH login')
    return 'Connection simulated'

# Handle frontend connection
@socketio.on('connect')
def handle_connect():
    print("Client connected")

if __name__ == '__main__':
    socketio.run(app, debug=True)
