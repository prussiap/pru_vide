#require 'temper_control'
require 'rubygems'
require 'ffi-rzmq'
require_relative 'lib/temp_control'

context = ZMQ::Context.new(1)

socket = context.socket(ZMQ::PUB)
socket.bind("tcp://127.0.0.1:6000")
control = TempControl.new target: 57.2, pulse_range: 10000, kp: 4.5, ki: 110, kd: 27.5
loop do
 	control.control_cycle
  socket.send_string((control.last_reading).to_s)
end
