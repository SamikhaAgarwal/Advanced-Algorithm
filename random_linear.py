# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 10:04:02 2018

@author: Samiksha Agarwal
"""

#%%
import random as rd
  
n=int(input("Enter the length of array you want"))
array=[]
for i in range(n):
    arr=int(input("Enter the array"))
    array.append(arr)
#%%
key=5
while True:
    rand_number=rd.randint(0,n-1)
    print(rand_number)
    if array[rand_number]==key:
        print("True")
        break
    else:
        print("False")
#%%
key=5
m=0
strial=10
while m < strial:
    rand_number=rd.randint(0,n-1)
    print(rand_number)
    if array[rand_number]==key:
        print("True")
        break
    else:
        print("False")
    m+=1    
  