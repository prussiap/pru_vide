require 'rubygems'
require 'em-zeromq'
require_relative 'temper_control'
require_relative 'lib/temp_control'

context = EM::ZeroMQ::Context.new(1)

EM.run {
  push_socket = context.socket(ZMQ::PUB)
  push_socket.bind("tcp://127.0.0.1:6000")
  control = TempControl.new target: 57.2, pulse_range: 10000, kp: 4.5, ki: 110, kd: 27.5

  pull_socket = context.socket(ZMQ::REP)
  pull_socket.bind("tcp://127.0.0.1:5000")

  pull_socket.on(:message) { |part|
    puts part.copy_out_string
    part.close
  }

  EM.add_periodic_timer(0) {
    control.control_cycle
  }

  EM.add_periodic_timer(0.1) {
    push_socket.send_msg(control.last_reading)
  }
}
