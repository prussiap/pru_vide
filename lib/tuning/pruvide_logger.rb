require "rubygems"
require "google_drive"
require 'csv'
require_relative "../../config/settings"

class PruvideLogger
    attr_accessor :current_file, :log_method, :current_file, :current_temperature, :pin_status

    def initialize(log_method, out_filename = "")
        @log_method = log_method
        if log_method == "google"
            @i = 1
            docs = Settings.settings[:docs]
            session = GoogleDrive.login(docs[:login], docs[:pass])
            @current_file = session.spreadsheet_by_key(docs[:key]).worksheets[0]
        elsif log_method == "csv"
            @current_file = CSV.open(Time.now.strftime("%Y_%m_%d_%Hh_%Mm_steady_output_tuning.csv"), 'wb')
        end
    end

    def log_me(current_temperature, pin_status, current_time)
        @current_temperature = current_temperature
        @pin_status = pin_status
        @current_time = current_time

        if log_method == "google"
            @i +=1
            docs_logging
        elsif log_method == "csv"
            csv_logging
        end
    end

    def csv_logging
        @current_file << [ @current_temperature, @pin_status, @current_time]
    end

    def docs_logging
        @ws[@i, 1] = @current_temperature
        @ws[@i, 2] = @pin_status
        @ws[@i, 3] = @current_time
        ws.save()
    end

end
