import spidev #hardware spi
# -*- coding: utf-8 -*-
#mkdir python-spi
#cd python-spi
#wget https://raw.github.com/doceme/py-spidev/master/setup.py
#wget https://raw.github.com/doceme/py-spidev/master/spidev_module.c
#sudo python setup.py install
import time
import math
from time import strftime
import string

temp_pin = 0

spi = spidev.SpiDev()
spi.open(0,1)# I set CS1 since i'm using CS0 for tt

# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
def readadc(adcnum):
    if ((adcnum > 7) or (adcnum < 0)):
        return -1
    r = spi.xfer2([1,(8+adcnum)<<4,0])
    adcout = ((r[1]&3) << 8) + r[2]
    return adcout

def ohm_to_celsius(x):                 
  A               = 0.00116597    
  B               = 0.000220635    
  C               = 1.81284e-06       
  D               = 2.73396e-09
  print x
  r = math.log(x)      
  return 1.0 / (A + B*r + C*r**2 + D*r**3) - 273.15

# calculate the resistence of the thermistor and compensate for voltage divider in the ADC aboard 
def volt_to_ohm(V):
  Rd = 10000       
  Rd_effective = (Rd * 16800.0) / (Rd + 16800.0)
  Rth = (5.0 - V) / V * Rd_effective
  return Rth

# read CHANNEL 1 on the ADC board
ADC1 = readadc(temp_pin)
ohm=volt_to_ohm(ADC1)
result=ohm_to_celsius(ohm)
print (result)
#def check_temp(tmp_pin): # check temperature and convert it to F
#        tmp_analog = readadc(tmp_pin)
#	R = 10000 / (1023 / (tmp_analog -1))
#        return str(R)
        
#print "The temp in your room is: " + check_temp(temp_pin) + " F"
