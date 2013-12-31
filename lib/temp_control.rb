require 'temper'
require_relative 'heating_element'
require_relative 'temperature_sensor'

class TempControl
    attr_reader :input, :output, :pid

    def initialize options = {}
      @pulse_range = options[:pulse_range] || 5000
      @input = TemperatureSensor.new
      @output = HeatingElement.new adapter: GPIO.new(pin: 17)
      configure_automatic_control options
    end

    def configure_automatic_control options
      @target = options[:target]
      @pid = Temper::PID.new maximum: @pulse_range
      @pid.tune 44, 165, 4
      @pid.setpoint = @target
    end

    def read_input
      reading = input.get_temp
      @last_reading = reading if reading
    end

    def calculate_power_level
      if read_input
        set_pulse_width pid.control @last_reading
      end
    end

    def set_pulse_width width
      if width
        output.pulse_width = width
      end
    end

    def control_cycle
      calculate_power_level
      output.pulse
    end
end
