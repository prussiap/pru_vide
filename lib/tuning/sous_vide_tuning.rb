require "rubygems"
require_relative "../temperature_sensor"
require_relative "../heating_element"
require 'pi_piper'
require_relative "pruvide_logger"

class SousVideTuning
    attr_accessor :temp_sensor, :current_temp, :start_time, :pin, :power, :pulse_width, :first_loop_min, :temp_array, :step_pulse_width, :sleep_time

    def initialize(pin, pulse_width, first_loop_min, new_pulse_width, sleep_time, log_type)
        @temp_sensor = TemperatureSensor.new.get_temp
        @current_temp = @temp_sensor.temperature

        @sleep_time = sleep_time
        @step_pulse_width = new_pulse_width
        @temp_array = []
        @start_time = Time.now
        @pin = PiPiper::Pin.new(:pin => pin, :direction => :out)
        @pin.off
        @log = PruvideLogger.new(log_type)
        @power = HeatingElement.new @pin
        @power.pulse_width pulse_width
        @first_loop_min = @start_time + (first_loop_min * 60)
    end

    def current_time
        (Time.now-@start_time)
    end

    def current_time_min
        current_time/60
    end

    def control_action
        @power.pulse
        pin_status = @pin.read
        curr_time = current_time_min
        @current_temp = @temp_sensor.get_temp
        current_values == [ @current_temp, pin_status, curr_time ]
        @temp_array << current_values
        @log.current_values(current_values[0], current_values[1], current_values[2])
        p "Current temp: #{@current_temp.temperature}, Status: #{pin_status}, Time: #{curr_time}"
        sleep @sleep_time
    end

    def is_steady?
        #calculate if temperature is stead
    end

    def log_and_loop_naive
        if Time.now < @first_loop_min
            control_action
        else
            @power.pulse_width @step_pulse_width
            control_action
        end
    end

end