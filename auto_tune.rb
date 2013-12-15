require_relative 'heating_element'
require 'temper'
require 'CSV'


file = CSV.open( "#{Time.now}_tuning\.csv", 'wb')


file << [setpoint, current_temperature, output, time]
