#!/usr/bin/env python3
#
#
# Simple test import lib
# Digital Liquid Level sensor switch,
# Model: GEMS ELS-950 LEVEL SWITCH (12V 40 mA)
#
# @Programmer: A. M:
# @ Date: 19-04-2019
#---------------------------


from liquid_level_function import *




if __name__ == "__main__":
	
	time_freq = 0.01 		# x.xxx ms/hz Frequency between the samples
	nbr_samples = 10 		# At least nbr_samples consecutive samples 
	# to validate a state (liquid or No liquid)

	l_level = liquid_level(nbr_samples, 0.001) #time_freq)
	print("## sensor 1: {}, sensor 2: {} ##".format(l_level[0], l_level[1]))
