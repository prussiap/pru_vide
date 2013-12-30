require_relative 'temper_control'
require 'rubygems'
require 'ffi-rzmq'

context = ZMQ::Context.new(1)

socket = context.socket(ZMQ::PUB)
socket.bind("tcp://127.0.0.1:6000")

control = TempControl.new target: 152.0
loop do
 	control.control_cycle
  socket.send_string(control.last_reading)
end
