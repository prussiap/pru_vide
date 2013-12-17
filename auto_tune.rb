require_relative 'lib/heating_element'
require "rubygems"
require "google_drive"
require_relative "lib/temperature_sensor"
require 'pi_piper'
include PiPiper

session = GoogleDrive.login("david@synteny.us", "Aquafina1")
ws = session.spreadsheet_by_key("0AgyFdwj_tPl_dG5pOXBjRWMxWGF1ZHRXNGxzTHVzZmc").worksheets[2]
setpoint = 50
temp = TemperatureSensor.new
start_time = Time.now
pin_status = 0
pin = PiPiper::Pin.new(:pin => 17, :direction => :out)
pin.off


i = 2
while true
	pv = temp.get_temp
	if pv.to_i > setpoint
		pin.off
		pin_status = 0
	else
		p "else"
		pin.on
		pin_status = 1
	end
	ws[i, 1] = setpoint
	ws[i, 2] = pv
	ws[i, 3] = pin_status
	ws[i, 4] = (start_time - Time.now)
	ws.save()
	i += 1
	p "Current temp: #{pv}, Setpoint: #{setpoint}, Status: #{pin_status}"
	sleep(5)
end

