from Adafruit_MCP230xx import Adafruit_MCP230XX
import sys
import time


if __name__ == '__main__':
    # ***************************************************
    # Set num_gpios to 8 for MCP23008 or 16 for MCP23017!
    # ***************************************************
    #mcp = Adafruit_MCP230XX(address = 0x20, num_gpios = 8) # MCP23008
    mcp = Adafruit_MCP230XX(address = 0x20, num_gpios = 16) # MCP23017

    # Set pins 0, 1 and 2 to output (you can set pins 0..15 this way)
#    mcp.config(4, mcp.OUTPUT) #LED if present
    mcp.config(7, mcp.OUTPUT) #SSR sous vide
    mcp.config(3, mcp.OUTPUT) 

    # Set pin 3 to input with the pullup resistor enabled
    mcp.pullup(2, 1) #Bottom button
    mcp.pullup(1, 1) #Second to bottom button

    # Read input pin and display the results
  #  print "Pin 3 = %d" % (mcp.input(6) >> 3)

    # Python speed test on output 0 toggling at max speed
    print "Starting blinky on pin 0 (CTRL+C to quit)"
    while (True):
        print "Pin 5 = %d" % (mcp.input(2))
        print "Pin 6 = %d" % (mcp.input(1))
 #       mcp.output(4, 1)  # Pin 0 High for led
        mcp.output(3, 1)
        mcp.output(7, 1)
        time.sleep(1);
  #      mcp.output(4, 0)  # Pin 0 Low
        mcp.output(3, 0)
        mcp.output(7, 0)
        time.sleep(1);
