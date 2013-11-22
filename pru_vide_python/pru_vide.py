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
#    mcp.config(0, mcp.OUTPUT)
#    mcp.config(1, mcp.OUTPUT)
    mcp.config(4, mcp.OUTPUT)
    mcp.config(3, mcp.OUTPUT)
    mcp.output(4, 0)

    # Set pin 3 to input with the pullup resistor enabled
    mcp.pullup(6, 1)
    mcp.pullup(5, 1)

    # Read input pin and display the results
  #  print "Pin 3 = %d" % (mcp.input(6) >> 3)

    # Python speed test on output 0 toggling at max speed
    print "Starting blinky on pin 0 (CTRL+C to quit)"
    while (True):
        print "Pin 5 = %d" % (mcp.input(5))
        print "Pin 6 = %d" % (mcp.input(6))
 #       mcp.output(4, 1)  # Pin 0 High
        mcp.output(3, 1)
        time.sleep(1);
  #      mcp.output(4, 0)  # Pin 0 Low
        mcp.output(3, 0)
        time.sleep(1);
