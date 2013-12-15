require_relative 'temper_control'

control = TempControl.new target: 152.0
loop do
 	control.control_cycle
end