# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 09:57:31 2018

@author: Samiksha Agarwal
"""

#%%
import numpy as np
class combo:
   
    def ask(self,number):
       
        mat=[]
  
        for i in range(number):
                print("Enter the order of matrix"+str(i+1))
                n=int(input("row length"))
                m=int(input("column length"))
                a=self.generate_matrix(n,m)
                print(a)
                mat.append(a)
        return mat
           
            
    def generate_matrix(self,n,m):
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
   
    def mat_add(self,a,b):
         c=np.asmatrix(np.full(np.shape(a),0))
         if np.shape(a)==np.shape(b):
             for i in range(np.shape(a)[0]):
                 for j in range(np.shape(a)[1]):
                     c[i,j]=a[i,j]+b[i,j]
         else:
              print("Dimensions of tthe matricies are not equal")            
         return c  
     
    def mat_mult(self,a,b):
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
               
#%%

def main():
    test_case=0
    comb=combo()
    while test_case<=20:
        try:
            add_mult=int(input("Press 1 for matrix_multiplication or Press 2 for matrix_addition"))
            if add_mult==1:
                number=int(input("Enter Number of Matrix you want"))
                try:
                    if number>1:
                        matrix=comb.ask(number)
                    else:
                        raise(ValueError)
                except ValueError:
                     print("take atleast two matrix")
                     number=int(input("Enter Number of Matrix you want"))
                     matrix=comb.ask(number)
                
            
                A=matrix[0]
                B=matrix[1]
                print("Result",comb.mat_mult(A,B))
               
                
                
            elif add_mult==2:
                number=int(input("Enter Number of Matrix you want"))
                
                matrix=comb.ask(number)
                A=matrix[0]
                B=matrix[1]
                print("Result",comb.mat_add(A,B))
               
            
            else:
                print("-----------------")
                print("Please enter either 1 or 2")
                print("-----------------")
                    
        except ValueError:
            print("-----------------")
            print("Please enter either 1 or 2")
            print("-----------------")
        
        finally:
            a=input("N to Exit. Press any key to continue...")
            if a=='N':
                break
            #ask_user=input("If you want to continue press y/Y")
            #if ask_user=='y' or ask_user=='Y':
            #    print("once again")
            #else:
            #    break
        test_case+=1
#%%
def trying(number):
    b=combo()
    try:
        if number<=1:
            raise(ValueError)
        else:
            mat=[]
            print("great choice")
            for i in range(number):
                print("Enter the order of matrix"+str(i+1))
                n=int(input("row length"))
                m=int(input("column length"))
                a=b.generate_matrix(n,m)
                print(a)
                mat.append(a)
            return mat
    except ValueError:
        print("please enter atleast 2 matrix")

             
    
    