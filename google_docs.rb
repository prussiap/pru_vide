require "rubygems"
require "google_drive"
require_relative "lib/temperature_sensor"
require 'pi_piper'
include PiPiper

# Logs in.
# You can also use OAuth. See document of
# GoogleDrive.login_with_oauth for details.
session = GoogleDrive.login("david@synteny.us", "Aquafina1")

# First worksheet of
# https://docs.google.com/spreadsheet/ccc?key=pz7XtlQC-PYx-jrVMJErTcg
#https://docs.google.com/spreadsheet/ccc?key=0AgyFdwj_tPl_dG5pOXBjRWMxWGF1ZHRXNGxzTHVzZmc&usp=sharing
ws = session.spreadsheet_by_key("0AgyFdwj_tPl_dG5pOXBjRWMxWGF1ZHRXNGxzTHVzZmc").worksheets[0]

temp = TemperatureSensor.new
start_time = Time.now
pin = PiPiper::Pin.new(:pin => 17, :direction => :out)
pin.on
# Changes content of cells.
# Changes are not sent to the server until you call ws.save().

i = 2
while true
	current_temperature = temp.get_temp
	ws[i, 1] = 100
	ws[i, 2] = current_temperature
	ws[i, 3] = "on"
	ws[i, 4] = (start_time - Time.now)
	ws.save()
	i += 1
	p "Current temperature: #{current_temperature}"
end

ws.reload()
