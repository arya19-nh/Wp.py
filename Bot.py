import eventlet
eventlet.monkey_patch()  # Ensure eventlet works properly

from flask import Flask
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # Allow external connections (Bubble.io)

@socketio.on("message")
def handle_message(msg):
    print(f"Received: {msg}")
    send(msg, broadcast=True)  # Send message to all users

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5003, debug=True)  # Changed port to 5001
