require 'rubygems'
require 'ffi-rzmq'

context = ZMQ::Context.new(1)

socket = context.socket(ZMQ::PUB)
socket.bind("tcp://127.0.0.1:6000")

msg = "menu smells like dog"

loop do
  puts "message sent"
  socket.send_string(msg)
  sleep(1)
end

