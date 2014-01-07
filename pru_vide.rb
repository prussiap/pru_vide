#require 'temper_control'
require 'rubygems'
require 'json'
require 'ffi-rzmq'
require_relative 'lib/temp_control'

pub_context = ZMQ::Context.new(1)
rep_context = ZMQ::Context.new

pub_socket = pub_context.socket(ZMQ::PUB)
pub_socket.bind("tcp://127.0.0.1:6000")

rep_socket = rep_context.socket(ZMQ::REP)
rep_socket.bind("tcp://127.0.0.1:5000")

control = TempControl.new target: 57.2, pulse_range: 10000, kp: 4.5, ki: 110, kd: 27.5
loop do
 	control.control_cycle
  to_ui = { temp: control.last_reading.to_s, time: control.current_time.to_s,
            set_point: control.target.to_s }.to_json
  pub_socket.send_string(to_ui)
#  rep_socket.recv_string(message = '')
#  p "blah4"
#  if message
#    p "if loop"
#    setpoint = JSON.parse(message)['setpoint']
#    control.target = setpoint
#    socket.send_string({ answer: 'success'}.to_json)
#  end
end
