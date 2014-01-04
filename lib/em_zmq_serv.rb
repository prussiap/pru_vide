require 'rubygems'
require 'em-zeromq'
require 'json'

context = EM::ZeroMQ::Context.new(1)

ctx = EM::ZeroMQ::Context.new(1)


class ControlMock
  attr_accessor :target

  def initialize
    @target = 50
  end
end

EM.run {
  puts "em run"

  socket = context.socket(ZMQ::SUB)
  socket.setsockopt(ZMQ::SUBSCRIBE, 'message')
  socket.connect("tcp://127.0.0.1:6000")
  control = ControlMock.new

  rep_sock = ctx.socket(ZMQ::REP)

  rep_sock.connect('tcp://127.0.0.1:9000')

  rep_sock.on(:message) { |part|
    puts "receive #{part.copy_out_string}"
    rep_sock.send_msg 'pong!'
    part.close
  }

  my_reply = "World"

  puts "it live"

  socket.on(:message) { |part|
    puts part.copy_out_string
    # puts "is message"
    # puts part.copy_out_string
    # ll = JSON.parse(part.copy_out_string)
    # if ll["msg"]
    #   puts ll["msg"]
    # elsif ll['setpoint']
    #   puts 'receive setpoint'
    #   control.target = ll['setpoint']
    # end
    # puts control.target
    part.close
  }

}
