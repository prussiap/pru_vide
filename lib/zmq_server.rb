require 'rubygems'
require 'ffi-rzmq'

context = ZMQ::Context.new

socket = context.socket(ZMQ::REP)
socket.bind("tcp://127.0.0.1:5000")

my_reply = "World"

loop do
  socket.recv_string(message = '')
  puts "Received request: #{message}"
  socket.send_string(my_reply)
end
