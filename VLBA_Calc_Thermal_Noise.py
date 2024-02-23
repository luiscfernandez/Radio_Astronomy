#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 10:26:16 2021

@author: Luis C. Fernandez
"""

import numpy as np


class VLBA_Thermal:

    def __init__(self, t_obs, antennas = 10,bandwidth = 512, npol = 2, nbit = 2, eta = 0.7, sefd = 210):

        """
        Initialize 
        Default Parameters 

        antennas = 10               # Number of antennas in use        
        bandwidth = 512             # MHz
        Npol = 2                    # Number of Polarizations
        Nbit = 2                    # Sampling rate (bit/sec)
        eta = 0.7                   # VLBI efficiency factor
        sefd = [210] * 10           # SEFD for each antenna (Dependent on Frequency; Currently set to 6cm)
                                      Possible values include: 289 ~21cm (L-Band)
                                                               314 ~18cm (L-Band)
                                                               210 ~6cm  (C-band)
                                                               327 ~4cm  (X-band)
                                                               543 ~2cm  (U-band)

        
        Input Variable:
        
        t_obs =                     # Integration Time (seconds)

        Output:

        Prints out the bandwidth, datarate, number of antennas, SEFD based on frequency
        for each antenna, and the theoretical noise for the given time


        """

        self.antennas = antennas
        self.t_obs = t_obs
        self.bandwidth = bandwidth
        self.npol = npol
        self.nbit = nbit
        self.eta = eta
        self.sefd = [sefd] * self.antennas

        return

    def noise(self):

        DATARATE = (self.bandwidth*self.npol*self.nbit*2) * 10**6 # bit/sec

        SEFD = 0
        for i in range(self.antennas):
    
            for j in np.arange(i+1,self.antennas):
        
                if i < j:
            
                    SEFD += 1/(self.sefd[i]*self.sefd[j])
            
                else:

                    break
            
        SEFD = 1/np.sqrt(SEFD)


        Noise = 1.0 / self.eta * SEFD / np.sqrt((DATARATE / 2.0) * self.t_obs) * 10**6 # micro Jy

        # Prints out Results

        print('Bandwidth used = ' + str(self.bandwidth) + ' MHz' )
        print('Datarate = '+str(round(DATARATE*10**(-6))) + r' Mbit/sec')
        print('Antennas used = ' + str(self.antennas) )
        print('SEFD for each antenna = ' + str(self.sefd[0]) + ' Jy')
        print('')
        print('Thermal Noise Estimate = '+str(round(Noise,2)) + u' \u03BCJy/beam')

        return
