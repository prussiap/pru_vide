import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:6000")
socket.setsockopt(zmq.SUBSCRIBE, "menu")

while True:
  print socket.recv()
