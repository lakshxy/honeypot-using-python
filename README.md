# Honeypot Using Python

This project simulates a honeypot application using Python with Flask and Socket.IO to log and display connection events in real-time.

## Features

- **Live Log Updates**: Real-time logs of events such as connection attempts and failed login attempts are displayed on the browser using Flask and Socket.IO.
- **Simulated Connections**: The Flask app simulates different types of connection events like SSH login attempts, which are logged and emitted to the frontend.
- **Real-Time Communication**: Flask with Socket.IO is used to stream the logs directly to the browser, ensuring that logs are updated as soon as they are generated.

## Setup Instructions

### Requirements

- Python 3.x
- Flask
- Flask-SocketIO

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/lakshxy/honeypot-using-python.git
   cd honeypot-using-python
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the App

1. **Start the Flask app**:
   ```bash
   python app.py
   ```

   This will start the Flask server and you can access the application at `http://127.0.0.1:5000/`.

2. **Simulate Events**:
   - Visit `http://127.0.0.1:5000/simulate_connection` to simulate a connection event and log it.
   
   - You can simulate different events by modifying the `simulate_connection()` route in `app.py` to log other types of events.

### Frontend

The frontend is kept simple and consists of a table where the logs will be dynamically updated as new logs are emitted by the Flask backend.

The `index.html` file can be easily edited if you want to customize the look and feel of the page. Feel free to update the HTML and CSS according to your preferences.

---

## Notes

- I kept this page simple so that you can easily modify it to suit your needs. You can update the layout, add more event types, or even customize the table structure as you see fit.
- The connection logs are displayed in a table with real-time updates. If you'd like to add more functionality or features, the structure is flexible enough to make such adjustments.

---

