require 'rubygems'
require 'em-zeromq'

context = EM::ZeroMQ::Context.new(1)

EM.run {
  puts "em run"
  socket = context.socket(ZMQ::PUSH)
  socket.connect("tcp://127.0.0.1:6000")

  msg = "menu smells like dog"
  puts "it live"

  EM.add_periodic_timer(1) {
    puts "attack"
    socket.send_msg("Hello")
  }

}
