#require 'temper_control'
require 'rubygems'
require 'json'
require 'temper'
require_relative 'lib/temp_control'

control = TempControl.new target: 57, pulse_range: 10000, kp: 4.5, ki: 110, kd: 27.5
loop do
 	control.control_cycle
end

#  rep_socket.recv_string(message = '')
#  p "blah4"
#  if message
#    p "if loop"
#    setpoint = JSON.parse(message)['setpoint']
#    control.target = setpoint
#    socket.send_string({ answer: 'success'}.to_json)
#  end
