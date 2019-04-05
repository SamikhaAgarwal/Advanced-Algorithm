# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 08:03:43 2018

@author: Samiksha Agarwal
"""

#%%
import numpy as np
a=[1,3,8,6,7,5,4,2,0]
n=int(len(a)/2)
L=a[:n]
R=a[n:]
b=np.zeros(len(a))
b=b.astype(int)
p,q,r=len(L),len(R),len(b)
#for (i,j,k) in zip(range(p),range(q),range(r)):
i=0
j=0
k=0
while i<p and j<q:    
    if L[i]<=R[j]:
        b[k]=L[i]
        i+=1
        #k+=1
    
    elif L[i]>R[j]:
        b[k]=R[j]
        j+=1
    k+=1
while i < p:
   b[k] = L[i]
   i += 1
   k += 1

    # Copy the remaining elements of R[], if there
    # are any
while j < q:
   b[k] = R[j]
   j += 1
   k += 1
    #%%
for (i,j,k) in zip(range(p),range(q),range(r)):
   print(i,j,k)    
#%%
# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]

a=[1,3,8,6,7,5,4,2,0]
def merge(arr,l,m,r):
   
    n1 = (m - l + 1)
    n2 = (r- m)
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[l + i]
        print("L",L)  
 
    for j in range(0 , n2):
        R[j] = arr[m + 1 + j]
        print("R",R)
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
    print('arr',arr)
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
            print("i",i)
            #print(L)
        else:
            arr[k] = R[j]
            j += 1
            print("j",j)
            #print(R)
        k += 1
        print(arr)
        print("k",k)

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        print('arr',arr)
        print("k",k)

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
        print(arr)
 #%%
# l is for left index and r is right index of the
# sub-array of arr to be sorted
def mergeSort(arr,l,r):
    if l < r:
 
        # Same as (l+r)/2, but avoids overflow for
        # large l and h
        m = int((l+(r-1))/2)
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
 #%%
 
# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
n = len(a)
print ("Given array is")
for i in range(n):
    print ("%d" %a[i])
 
mergeSort(a,0,n-1)
print ("\n\nSorted array is")
for i in range(n):
    print ("%d" %a[i]),
    
        