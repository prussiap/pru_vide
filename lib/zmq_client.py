import zmq
#rep/req socket to sennd button info to controller
context = zmq.Context()
socket = context.socket(zmq.REQ) #reply/request socket
socket.connect("tcp://127.0.0.1:5000")

msg = "Hello"
socket.send(msg)
msg_in = socket.recv()

print "msg is: %s" % msg_in
