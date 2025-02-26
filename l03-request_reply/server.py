import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://localhost:5556") # conecta no broker local
msg_count = 0

hb_socket = context.socket(zmq.REQ)
hb_socket.connect("tcp://localhost:5557")
hb_msg_count = 0

poller = zmq.Poller()
poller.register(socket, zmq.POLLIN)

heartbeat_interval = 5  # seconds
last_heartbeat_time = time.time()

while True:
    socks = dict(poller.poll(1000))  # Poll every second

    if socket in socks and socks[socket] == zmq.POLLIN:
        try:
            message = socket.recv(zmq.NOBLOCK)
            print(f"Mensagem {msg_count}:", end=" ")
            socket.send_string("World")
            print(f"{message}")
            msg_count += 1
        except zmq.Again:
            pass  # No message received

    current_time = time.time()
    if current_time - last_heartbeat_time >= heartbeat_interval:
        print(f"Enviando heartbeat {hb_msg_count}")
        hb_socket.send_string("Heartbeat")
        hb_msg_count += 1
        hb_socket.recv()
        last_heartbeat_time = current_time
