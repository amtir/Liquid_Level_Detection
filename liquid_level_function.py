#!/usr/bin/env python3
#
# Digital Liquid Level sensor switch,
# Model: GEMS ELS-950 LEVEL SWITCH (12V 40 mA)
#
# @Programmer: A. M:
# @ Date: 19-04-2019
#---------------------------

'''
Liquid detection: Interfacing the ELS-950 the electro-optic liquid level sensor. (Python)

The ELS-950 is an excellent value making it a perfect choice for industrial OEMs desiring an extremely small, 'no-moving-parts' sensor rated for high temperatures. 
Operating temperature capability up to 230°F (110°C). 

Applications:
Coolant reservoir monitor and warning
Medical diagnostic, sterilizer, washers and dialysis equipment
Low lubricant warning on machine tools, generator sets, on- or off-highway vehicles
Low level warning in hydraulic reservoirs 
Plastic overflow bottles, plastic radiators 
'''

import time
import datetime
import RPi.GPIO as GPIO
from multiprocessing import Process, Pipe, Array, Value
import sys, os, glob
import matplotlib.pyplot as plt



GPIO.setwarnings(False)         					
GPIO.cleanup()											
GPIO.setmode(GPIO.BOARD)

# Sensors GPIO
liquid_level_1_gpio = 18 
liquid_level_2_gpio = 22

GPIO.setup( liquid_level_1_gpio, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup( liquid_level_2_gpio, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)




def liquid_level(nbr_samples, time_freq):
	
	count= 0; sens1 = 1; sens2=1;
	while (count < nbr_samples):
		sens1 = (1 ^ GPIO.input(liquid_level_1_gpio)) & sens1
		sens2 = (1 ^ GPIO.input(liquid_level_2_gpio)) & sens2
		#print('{0} , {1} , {2}'.format(time.time(), sens1, sens2)) # CSV format
		count = 1 + count
		time.sleep(time_freq)
	
	return [sens1, sens2]




'''
if __name__ == "__main__":
	time_freq = 0.01 		# x.xxx ms
	nbr_samples = 10 		# At least nbr_samples consecutive samples to validate a state (liquid or No liquid)

	l_level = liquid_level(nbr_samples, 0.001) #time_freq)
	print("sensor 1: {}, sensor 2: {}".format(l_level[0], l_level[1]))
'''

   




