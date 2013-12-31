require 'rubygems'
require 'em-zeromq'

context = EM::ZeroMQ::Context.new(1)

EM.run {

  socket = context.socket(ZMQ::PULL)
  socket.bind("tcp://127.0.0.1:6000")

  my_reply = "World"

  socket.on(:message) { |part|
    puts part.copy_out_string
    part.close
  }

}
