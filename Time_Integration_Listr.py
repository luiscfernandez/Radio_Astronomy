#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 15:40:25 2022

@author: Luis C. Fernandez
"""

import numpy as np
import os

###############################################################################
###############################################################################
# Input Parameters

#Object
source = 'NGC3079'

# Either 'seconds' or 'minutes'
param = 'seconds' 

# Folder location that contains *.listr file(s) from AIPS task Listr OPTYPE 'SCAN'
Folder = os.listdir('./')
                  

###############################################################################
###############################################################################
# Do not touch any code below
###############################################################################
###############################################################################
Files = []

for file in Folder:
    
    if file.endswith(".listr") and source in file:
        Files.append(os.path.join(file))
        
Files = sorted(Files)

def Listr_time(File,param):
                                             
    t1 = []
    t2 = []
    # Sift through txt file to obtain times only and throw away everything else
    
    with open(File, "r") as target_file:        
        
        for line in target_file:
            
            if source in line and 'File' not in line:
                
                t1.append(line.split()[5].replace("/",":").split(':'))
                t2.append(line.split()[7].replace("/",":").split(':'))
            elif line.strip() == "Source summary":
                break
            else:
                continue
    
    # Find Number of observations
    n = len(t1)
    t1 = np.array(t1)
    t2 = np.array(t2)
    #print(n)
    #print(t2)
        
    #print(t)            
    #Initialize array for minutes and seconds

    time_min = []
    time_sec = []

    # Loop to split time to hours,min,sec and calculate time difference between start/stop
    for i in range(n):
        
        diff = np.array([int(t2[i][0])-int(t1[i][0]),int(t2[i][1])-int(t1[i][1]),
                         int(t2[i][2])-int(t1[i][2]),int(t2[i][3])-int(t1[i][3])])
        
        
        total_min = diff[0]*24*60 + diff[1]*60 + diff[2] + diff[3]/ 60
        total_sec = diff[0]*24*60*60 + diff[1]*60*60 + diff[2]*60 + diff[3]
            
        time_min.append(total_min)
        time_sec.append(total_sec) 
        
    time_min = np.sum(time_min)
    time_sec = np.sum(time_sec)
    
    if param == 'minutes':
        total_time = time_min
    
    elif param == 'seconds':
        
        total_time = time_sec
    
    return total_time
###############################################################################
###############################################################################   

N = len(Files)

for i in range(N):
    print('For ' + Files[i].split('_')[0])
    print('Total time of observation ' + str(round(Listr_time(Files[i],param),2)) + ' ' + param + '\n' )
    
