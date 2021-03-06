require_relative '../config/settings.rb'

class TemperatureSensor
	attr_reader :temperature, :temp_device

	def initialize
    @temp_device = Settings.settings[:devices][:device1][:temp_probe_address]
		modprobe = `sudo modprobe w1_gpio && sudo modprobe w1_therm`
		device_list =  `ls -l /sys/bus/w1/devices/`
	end

	def get_temp
		temp = `cat /sys/bus/w1/devices/#{temp_device}/w1_slave`
		my_split = temp.split("\n")
		if my_split[0][-3..-1] =="YES"
			temp = my_split[1].split("=")[1]
			@temperature = temp.to_f/1000
		else
			@temperature = nil
		end
	end

	def to_temp_f
		(@temperature * 9.0 ) / 5.0 + 32.0
	end
end
