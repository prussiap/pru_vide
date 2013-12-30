require_relative 'lib/temp_control'

control = TempControl.new target: 57.2, pulse_range: 10000, kp: 4.5, ki: 110, kd: 27.5
loop do
 	control.control_cycle
end
