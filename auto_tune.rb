require_relative 'heating_element'
require "rubygems"
require "google_drive"
require 'csv'
require_relative "lib/temperature_sensor"
require 'pi_piper'
include PiPiper


setpoint = 50
temp = TemperatureSensor.new
start_time = Time.now
pin_status = 0
pin = PiPiper::Pin.new(:pin => 17, :direction => :out)
pin.on

my_file = CSV.open("#{Time.now}_autotune.csv", 'wb')

i = 2
while true
	pv = temp.get_temp
	if pv.to_i > setpoint
		pin.off
		pin_status = 0
	else
		pin.on
		pin_status = 1
	end
	my_file << [ setpoint, pv, pin_status, (start_time - Time.now) ]
	i += 1
	sleep(5)
end




