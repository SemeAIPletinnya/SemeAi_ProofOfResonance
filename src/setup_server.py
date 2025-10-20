import socketio
import eventlet
from datetime import datetime

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)

connected_clients = set()

@sio.event
def connect(sid, environ):
    connected_clients.add(sid)
    print(f"[{datetime.now()}] Resonant node connected: {sid}")
    sio.emit("resonance_update", {"message": f"Node {sid} joined the Resonance Network."})

@sio.event
def disconnect(sid):
    connected_clients.discard(sid)
    print(f"[{datetime.now()}] Resonant node disconnected: {sid}")

@sio.on('pulse')
def handle_pulse(sid, data):
    timestamp = datetime.now().isoformat()
    print(f"[Pulse] {timestamp}: {data}")
    sio.emit('pulse_broadcast', {"from": sid, "timestamp": timestamp, "data": data})

def start_server():
    print("🌐 Resonance Socket.IO Server running on http://localhost:8080")
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 8080)), app)

if __name__ == "__main__":
    start_server()
