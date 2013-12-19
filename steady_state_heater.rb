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
power.pulse_width = 1500

run_1_time = start_time + (60 * 60)

my_file = CSV.open("#{Time.now.strftime("%m_%d_%H_%M")}_steady_state_heater.csv", 'wb')

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
