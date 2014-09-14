require "rubygems"
require "json"


def load_settings( filename )
  File.open( filename, "r" ) do |f|
    JSON.load( f )
  end
end


settings = load_settings( "config/settings.json" )
p settings['blah']
