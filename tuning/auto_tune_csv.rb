require "rubygems"
#require "google_driver"
require 'csv'
require_relative 'lib/temperature_sensor.rb'
require 'pi_piper'
include PiPiper

temp = TemperatureSensor.new
start_time = Time.now
pin = PiPiper::Pin.new(:pin => 17, :direction => :out)
pin.on
# Changes content of cells.
# Changes are not sent to the server until you call ws.save().
my_file = CSV.open("#{Time.now}_autotune.csv", 'wb')

while true
        pv = temp.get_temp
        my_file << [ 50, pv, "on", start_time - Time.now]
        p "Current temperature is #{pv}oC"
        sleep(5)
end