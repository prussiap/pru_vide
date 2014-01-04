require 'rubygems'
require 'em-zeromq'
require_relative 'temper_control'
require_relative 'lib/temp_control'

# presets hash for menu
@listings = {  pork: 60,
              duck: 50,
              eggs: 61
}

context = EM::ZeroMQ::Context.new(1)

EM.run {
  push_socket = context.socket(ZMQ::PUB)
  push_socket.bind("tcp://127.0.0.1:6000")

  # default values for startup -- for now, needs to be set manually by
  # SSHing in.
  control = TempControl.new target: 57.2, pulse_range: 10000, kp: 4.5, ki: 110, kd: 27.5

  rep_socket = context.socket(ZMQ::REP)
  rep_socket.connect("tcp://127.0.0.1:5000")

  # takes a hash from JSON.
  # to update target temperature, hash needs a "setpoint" key
  # and the new target temperature as it's associated value.
  # to retrieve menu listing hash, send a "menu" key, value is unused.
  rep_sock.on(:message) { |part|
    parsed_message = JSON.parse(part.copy_out_string)
    if parsed_message['setpoint']
      rep_sock.send_msg('received setpoint')
      control.target = parsed_message['setpoint']
      puts "new target #{control.target}"
    elsif parsed_message['menu']
      rep_sock.send_msg("#{{msg: @listings}.to_json}")
    end
    part.close
  }

  # loops control cycle
  EM.add_periodic_timer(0) {
    control.control_cycle
  }

  # sends current observed temperature via PUB socket
  EM.add_periodic_timer(0.1) {
    push_socket.send_msg(control.last_reading)
  }
}
