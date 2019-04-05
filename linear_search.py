#%%
def Linear_search(L,e):
  for i in range(len(L)):
     if L[i]==e:
        
       
        print(i)
        print( 'True')
        
     if L[i]>e:
        return False
  return False  

L=[6,8,9,9,5,9,8]
Linear_search(L,9)           
#%%
# Function to do insertion sort
def Insertion_Sort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
        print("key",key)
        print('arr',arr)
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
                print(j)
        arr[j+1] = key
        print('arr',arr)
        print('i',i)
 
 
# Driver code to test above
arr = [12, 11, 13, 5, 6,6,9,6]
Insertion_Sort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i])
 