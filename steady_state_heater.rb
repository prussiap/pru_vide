require_relative 'lib/heating_element'
require "rubygems"
#require "google_drive"
require 'csv'
require_relative "lib/temperature_sensor"
require 'pi_piper'
include PiPiper
require 'wiringpi'

temp = TemperatureSensor.new
start_time = Time.now
pin_status = 0
pin = PiPiper::Pin.new(:pin => 17, :direction => :out)
pin.off
power = HeatingElement.new pin
power.pulse_width = 1000
run_1_time = start_time + (60 * 60)

my_file = CSV.open("#{Time.now.strftime("%m_%d_%h_%m")}_rice_cooker_steady_state_heater.csv", 'wb')

loop do
	pin_status = pin.read
	pv = temp.get_temp
	if Time.now < run_1_time
		power.pulse
		my_file << [ pv, pin_status, (Time.now - start_time)/60]
		p "Current temp: #{pv}, Status: #{pin_status}, Time: #{(Time.now - start_time)/60}"
		sleep 0.5
	else
		power.pulse_width = 2000
		power.pulse
		my_file << [ pv, pin_status, (Time.now - start_time)/60 ]
		p "Current temp: #{pv}, Status: #{pin_status}, Time: #{(Time.now - start_time)/60}"
		sleep 0.5
	end
end

# while true
# 	pv = temp.get_temp
# 	if pin.on?
# 		pin.off
# 		pin_status = 0
# 	else
# 		pin.on
# 		pin_status = 1
# 	end
# 	my_file << [ setpoint, pv, pin_status, (start_time - Time.now) ]
# 	p "Current temp: #{pv}, Status: #{pin_status}"
# 	sleep 1
# end


# power in 0.2 steps
# percent of 5sec pulse time power is on
# pin on, sleep 5/power
# for remainder of time, power off
