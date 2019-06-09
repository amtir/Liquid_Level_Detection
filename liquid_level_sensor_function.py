#!/usr/bin/env python3
#
# Digital Liquid Level sensor switch,
# Model: GEMS ELS-950 LEVEL SWITCH (12V 40 mA)
#
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

#
# @Programmer: A. M:
# @ Date: 19-04-2019
#---------------------------

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


#time_period_Sec = 10 	# Time period in Seconds [S]
time_freq = 0.01 		# 10ms
nbr_samples = 50 		# At least 10 consecutive samples

strDate = '{0:%Y-%m-%d_%H-%M-%S}'.format(datetime.datetime.now())
file_name = "liquid_level_Sensor_log_"+ strDate +".csv"


LiquidLevelSens = {'t':[], 'y':[]}
LiquidLevelSens2 = {'t':[], 'y':[]}




# Open a file
fo = open(file_name, "w")

start = time.time()
count=0
sens1 = 1

#while (time.time() - start) <= time_period_Sec:
while (count < nbr_samples):
    sens1 = (1 ^ GPIO.input(liquid_level_1_gpio)) & sens1
    sens2 = (1 ^ GPIO.input(liquid_level_2_gpio)) & sens1  
    print('{0} , {1} , {2}'.format(time.time(), sens1, sens2)) # CSV format
    
    count = 1 + count

    (LiquidLevelSens['t']).append( count )
    (LiquidLevelSens['y']).append( sens1 )
    
    (LiquidLevelSens2['t']).append( count )
    (LiquidLevelSens2['y']).append( sens2 )
    
    fo.write('{0} , {1}, {2}'.format(time.time(), sens1, sens2 ) + "\n");
    
    # Sleep for xxx milliseconds.
    time.sleep(time_freq)

# Close opend file
fo.close()
print("Log file name: " + file_name + " created.")

str_x_label = 'time [{}S]'.format(time_freq)
plt.plot(LiquidLevelSens['t'], LiquidLevelSens['y'], 'gs--' ,  label='liquid sensor 1')
plt.plot(LiquidLevelSens2['t'], LiquidLevelSens2['y'],  'bs--' , label='liquid sensor 2')
plt.ylabel('0 ==> No Liquid    -    Liquid ==> 1')
plt.xlabel(str_x_label)
plt.title('Digital Liquid Level sensor')
plt.legend()
plt.show()

print("Program terminated.")



   




