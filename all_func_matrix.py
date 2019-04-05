# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 21:32:52 2018

@author: Samiksha Agarwal
"""

#%%def generate_matrix(n,m):
    matrix=np.asmatrix(np.full((n,m),0))
    for i in range(n):
        for j in range(m):
            try:
                a=int(input('Enter Number'))
                matrix[i,j]=a
            except ValueError:
                print("Please enter a number")
                a=int(input('Enter Number'))
                matrix[i,j]=a
    return matrix    
#%%
matrix=np.asmatrix(np.full((2,2),0))

for i in range(2):
    for j in range(2):
        a=input("enter input")
        matrix[i,j]=a
#%%
def ask(number):
    mat=[]
    for i in range(number):
        print("Enter the order of matrix"+str(i+1))
        n=int(input("row length"))
        m=int(input("column length"))
        a=generate_matrix(n,m)
        print(a)
        mat.append(a)
    return mat     
#%%
a=generate_matrix(2,2)  
#%%    
b=generate_matrix(1,2)             
#%%
def mat_add(a,b):
     c=np.asmatrix(np.full(np.shape(a),0))
     if np.shape(a)==np.shape(b):
         for i in range(np.shape(a)[0]):
             for j in range(np.shape(a)[1]):
                 c[i,j]=a[i,j]+b[i,j]
     else:
          print("Dimensions of tthe matricies are not equal")            
     return c        
#%%
def mat_mult(a,b):
      if np.shape(a)[1]==np.shape(b)[0]:
        c=np.asmatrix(np.full((np.shape(a)[0],np.shape(b)[1]),0))
        # row of A
        for i in range(np.shape(a)[0]):
            # column of B
             for j in range(np.shape(b)[1]):
                 # row of B
                 for k in range(np.shape(b)[0]):
                         c[i,j]+=a[i,k]*b[k,j]
        return c 
      else:
          print("ValueError: shapes"+ str(np.shape(a)) + "and" + str(np.shape(b))+"not aligned") 