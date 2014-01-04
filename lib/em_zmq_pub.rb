require 'rubygems'
require 'em-zeromq'
require 'json'

context = EM::ZeroMQ::Context.new(1)

ctx = EM::ZeroMQ::Context.new(1)

EM.run {
  puts "em run"
  socket = context.socket(ZMQ::SUB)
  socket.setsockopt(ZMQ::SUBSCRIBE, '')
  socket.connect("tcp://127.0.0.1:6000")

  req_sock = ctx.socket(ZMQ::REQ)
  req_sock.bind('tcp://127.0.0.1:9000')

  msg = "menu smells like dog"
  puts "it live"
  i = 50

  # EM.add_periodic_timer(3) {
  #   puts "sending ping"
  #   req_sock.send_msg({msg: 'ping'}.to_json)
  # }
  req_sock.on(:message) { |part|
    puts "is message"
    ll = JSON.parse(part.copy_out_string)
    puts ll['msg']
  }

  socket.on(:message) { |part|
    puts part.copy_out_string
  }

  # EM.add_periodic_timer(1) {
  #   puts "sending hello"
  #   socket.send_msg('message of hello')
  # }

  EM.add_periodic_timer(7) {
    puts "sending setpoint"
    socket.send_msg("message of setpoint is #{i+=1}")
  }

  EM.add_periodic_timer(3) {
    puts "sending menu request"
    req_sock.send_msg("#{{menu:"menu"}.to_json}")
  }

  EM.add_periodic_timer(12) {
    puts "sending new setpoint"
    req_sock.send_msg("#{{setpoint:55}.to_json}")
  }

}
