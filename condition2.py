# -*- coding: utf-8 -*-
"""
Created on Wed May 27 01:20:28 2026

@author: Aaryan
"""

import time
timestamp=int(time.strftime("%H:%M:%S")
print("The Time is: ", timestamp) 
timestamp2 = int(time.strftime("%H"))

if timestamp2 >= 21 or timestamp2 < 4:
    print("***GOOD NIGHT !!!***")
elif timestamp2 >= 17:
    print("*****GOOD EVENING !!!*****")
elif timestamp2 >= 12:
    print("*****GOOD AFTERNOON !!!*****")
else:
    print("***GOOD MORNING !!!***")
