# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 11:17:37 2018

@author: Samiksha Agarwal
"""

#%%
def linear(L,e):
    for i in range(len(L)):
        if L[i]==e:
            return True
        if L[i]>e:
            return False
    #return False     
L=['s','a','m','i','k']
#l=[s,a,m,i]
linear(L,e)
#%%
l=[4,5,2,8,9,3,0]
pivot=4

low=0
high=6

while (low<high):
    while l[low]<=pivot:
        low+=1
        print(low,high)
#%%

# Python program for implementation of Quicksort Sort
 
# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr):
    i = ( low-1 ) 
    high=random.randint(0,n-1)            # index of smaller element
    pivot = arr[high]     # pivot
    j=0
    #for j in range(low , high):
    while True:
 
        # If current element is smaller than or
        # equal to pivot
        if   arr[j] <= pivot:
         
            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
            j+=1
 
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )
 
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
 
# Function to do Quick sort
def quickSort(arr,low,high):
    high=random.randint(0,4)    
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)     
#%%
# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),       
#%%
import numpy as np
import random
random.randint(0,4)    