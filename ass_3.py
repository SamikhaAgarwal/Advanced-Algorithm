# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 10:28:26 2018

@author: Samiksha Agarwal
"""

#%%
import math
p=math.log2(2)
def log_logn(num):
    i=0
    while num>0:
            #print("num",num)
       
            n=math.log2(num)
            print("n",n)
            if n>0 and n<=1:
                i+=1
                print("Number of steps",i)
                break
            log=math.log2(n)
            print("log*logn =", log)
            
                
            num=n
            i+=1
#%%
def log2(num):
   log1=math.log2(log_logn(num))  
   print(log1)
             
        
        