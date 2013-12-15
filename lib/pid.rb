class Pid
	# constants

	# terms

	attr_accessor :input, :output, :setpoint, :kp, :ki, :kd
	attr_accessor :controller_direction, :in_auto, :sample_time
	attr_accessor :iterm, :out_max, :out_min, :last_input

	def initialize(input, output, setpoint, kp, ki, kd, controller_direction)
		@input = input
		@output = output
		@setpoint = setpoint
		@in_auto = false

		brett_initialize
		set_output_limits(1, 100) #PWM limits for Raspberry pi
		@sample_time = 100.to_f
		
		set_controller_direction(controller_direction)
		set_tunings

		last_time = millis - sample_time

	end

	def set_controller_direction(direction)
		if (@in_auto && direction) != direction
			
	end

	def brett_initialize
		@iterm = @output
		@last_input = @input
		@iterm = out_max if @iterm > out_max
	end

	def set_output_limits(min, max)
		return if min >= max
		@out_min = min
		@out_max = max

		if @in_auto
			@output = @out_max if @output > @out_max
			@output = @out_min if @output < @out_min

			@iterm = @out_max if @iterm > @out_max
			@iterm = @out_min if @iterm < @out_max
		end
	end

	def set_tunings(kp, ki, kd)
		return if (@kp<0 || @ki<0 || @kd<0)
		disp_kp = kp
		disp_ki = ki
		disp_kd = kd

		sample_time_in_sec = @sample_time/1000.0
		@kp = kp
		@ki = ki * sample_time_in_sec
		@kd = kd / sample_time_in_sec

		if @controller_direction == "REVERSE"
			@kp = (0 - @kp)
			@ki = (0 - @ki)
			@kd = (0 - @kd)
		end
	end


end
