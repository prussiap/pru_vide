require 'rubygems'
require 'em-zeromq'
require 'json'

context = EM::ZeroMQ::Context.new(1)

ctx = EM::ZeroMQ::Context.new(1)

@listings = {  pork: 60,
              duck: 50,
              eggs: 61
}

class ControlMock
  attr_accessor :target

  def initialize
    @target = 50
  end
end

EM.run {
  puts "em run"

  socket = context.socket(ZMQ::PUB)
  socket.bind("tcp://127.0.0.1:6000")
  control = ControlMock.new

  rep_sock = ctx.socket(ZMQ::REP)

  rep_sock.connect('tcp://127.0.0.1:9000')

  rep_sock.on(:message) { |part|
    parsed_message = JSON.parse(part.copy_out_string)
    if parsed_message["msg"]
      puts parsed_message["msg"]
    elsif parsed_message['setpoint']
      puts 'receive setpoint'
      control.target = parsed_message['setpoint']
      puts "new target #{control.target}"
    elsif parsed_message['menu']
      rep_sock.send_msg("#{{msg: @listings}.to_json}")
    end
    part.close
  }

  my_reply = "World"

  puts "it live"

  EM.add_periodic_timer(3) {
    socket.send_msg(control.target.to_s)
  }

}
