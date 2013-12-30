require 'temper'
require_relative 'heating_element'
require_relative 'temperature_sensor'
require 'pi_piper'
require_relative 'tuning/pruvide_logger'

class TempControl
    attr_reader :input, :output, :pid, :kp, :ki, :kd, :log, :start_time

    def initialize options = {}
      @pulse_range = options[:pulse_range] || 5000
      @kp = options[:kp]
      @ki = options[:ki]
      @kd = options[:kd]
      @log = PruvideLogger.new('csv')
      @input = TemperatureSensor.new
      @start_time = Time.now
      @output = HeatingElement.new adapter: PiPiper::Pin.new(:pin => 17, :direction => :out)

      configure_automatic_control options
    end

    def current_time
        (Time.now-@start_time)
    end

    def current_time_min
        current_time/60
    end

    def configure_automatic_control options
      @target = options[:target]
      @pid = Temper::PID.new maximum: @pulse_range
      @pid.tune @kp, @ki, @kd
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
      curr_time = current_time_min
      @log.log_me(@last_reading,'ignore', curr_time)
      p "Current temp: #{@last_reading}, Time: #{curr_time}"
      output.pulse
    end
end
