# -*- coding: utf-8 -*-
"""
Created on Wed May 27 01:05:56 2026

@author: Aaryan
"""

a=int(input("Enter Your Number : "))
if a<0 :
    print("Number is Negative")
elif a>0 :
    if (a>=1 and a<10):
        print("It is a One digit Positive Number")
    elif (a>=10 and a<100):
        print("It is a Two digit Positive Number")
    else :
        print ("It is a positive Number")
else: 
    print("The Number is Zero !")
        