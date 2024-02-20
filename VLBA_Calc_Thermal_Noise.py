#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 10:26:16 2021

@author: Luis C. Fernandez
"""

import numpy as np

###############################################################################
# Parameters to change

antennas = 10               # Number of antennas in use
T_obs =  2905               # Integration Time (seconds)
bandwidth = 384             # MHz
Npol = 2                    # Number of Polarizations
Nbit = 2                    # Sampling rate (bit/sec)
eta = 0.7                   # VLBI efficiency factor
SEFD_6cm = [210] * 10       # SEFD for each antenna (Dependent on Frequency; 6cm)


###############################################################################
###############################################################################
# Do not change below; Calculations for Thermal Noise
###############################################################################
###############################################################################

DATARATE = (bandwidth*Npol*Nbit*2) * 10**6 # bit/sec

SEFD = 0
for i in range(antennas):
    
    for j in np.arange(i+1,antennas):
        
        if i < j:
            
            SEFD += 1/(SEFD_6cm[i]*SEFD_6cm[j])
            
        else:
            break
            
SEFD = 1/np.sqrt(SEFD)


Noise = 1.0 / eta * SEFD / np.sqrt((DATARATE / 2.0) * T_obs) * 10**6 # micro Jy


###############################################################################
###############################################################################
# Prints out Results

print('Bandwidth used = ' + str(bandwidth) + ' MHz' )
print('Datarate = '+str(round(DATARATE*10**(-6))) + r' Mbit/sec')
print('Antennas used = ' + str(antennas) )
print('SEFD for each antenna = ' + str(SEFD_6cm[0]) + ' Jy')
print()
print('Thermal Noise Estimate = '+str(round(Noise,2)) + u' \u03BCJy/beam')




theoretical = np.array([28.57,19.96,24.16,19.99])

theo_avg = 1 / np.sqrt(sum(1/(theoretical)**2))
