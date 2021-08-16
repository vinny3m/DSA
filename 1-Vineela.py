#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Insertion sort

array=[]
n=int(input("enter the no of elements to be sorted: "))
for i in range(0, n):
    element = int(input())
    array.append(element)

print("The array to be sorted is:",array)


def insertion_sort(A):
    for l in range(1,n):
        temp=A[l]
        
        m=l-1;
        
        while m>=0 and A[m]>temp:
            A[m+1]=A[m]
            m-=1
        A[m+1]=temp

insertion_sort(array)
print("\nThe sorted list is:", array)


# In[7]:


# Merge Sort


import math
import numpy as np

p=np.inf #positive infinity value
arr=[]
n=int(input("enter the no of elements to be sorted: "))
for i in range(0, n):
    element = int(input())
    arr.append(element)

print("The array to be sorted is:", arr)


def merge(arr, lv, mid, uv):
    n1 = mid - lv + 1 #length of left elements
    n2 = uv - mid   #length of right elements
    #initiation of temporary left and right arrays
    R=[] 
    L=[]

    for i in range(0,n1):
        ele=arr[lv+i]
        L.append(ele)
    for i in range(0,n2):
        ele=arr[mid+i+1]
        R.append(ele)
    
    #setting the value as infinity 
    L.append(p)
    R.append(p)
          
    i=0
    j=0
   
    
    for k in range(lv,uv+1):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1

def merge_sort(arr, lv, uv):
    if lv < uv:
        mid = (lv+uv)//2
        merge_sort(arr, lv, mid)
        merge_sort(arr, mid+1, uv)
        merge(arr, lv, mid, uv)




merge_sort(arr, 0, n-1)
print("\n The sorted array is" , arr)


# In[ ]:




