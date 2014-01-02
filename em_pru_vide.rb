require 'rubygems'
require 'em-zeromq'
require_relative 'temper_control'
require_relative 'lib/temp_control'

context = EM::ZeroMQ::Context.new(1)

EM.run {
  socket = context.socket(ZMQ::PUSH)
  socket.bind("tcp://127.0.0.1:6000")
  control = TempControl.new target: 57.2, pulse_range: 10000, kp: 4.5, ki: 110, kd: 27.5

  EM.add_periodic_timer(0) {
    control.control_cycle
  }

  EM.add_periodic_timer(0.1) {
    socket.send_string(control.last_reading)
  }
}
