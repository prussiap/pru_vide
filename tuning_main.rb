require "rubygems"
require_relative "lib/tuning/sous_vide_tuning"

pin             = 17
pulse_width     = 1500 #mseconds
frist_loop_min  = 60   #minutes
new_pulse_width = 2000 #mseconds
sleep_time      = 0.5  #seconds
log_type        = "csv" # could be google

sous_vide_tuning = SousVideTuning.new(pin, pulse_width, first_loop_min, new_pulse_width, sleep_time, log_type)

loop do
    sous_vide_tuning.log_and_loop_naive
end