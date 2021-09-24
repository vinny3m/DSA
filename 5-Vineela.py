#!/usr/bin/env python
# coding: utf-8

# # Comparision of bucket sort and quick sort for floating point numbers in range 0 to 1
# 

# In[1]:


#Comparision of bucket sort and quick sort for floating numbers in range 0 to 1.

import math 
import time
import matplotlib.pyplot as plt
import random
import numpy as np


#bucket sort
def insertionSort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i-1
        while j >=0 and A[j] > key:
            A[j+1] = A[j]
            j = j - 1
        A[j+1]= key


def bucketSort(A):
    buc = []
    n = len(A)
    
    #An empty linked list is created
    for i in range(n):
        buc.append([])
        
    #keep the values in their respective buckets
    for element in A:
        index = math.floor(n*element)
        buc[index].append(element)
        
    #Sorting the buckets using insertion sort. 
    for b in buc:
        b = insertionSort(b)
        
    #concatinating the lists(buckets) in order.
    i=0
    for b in buc:
        for ele in b:
            A[i] = ele
            i += 1

rangee=[10,100,1000,10000,100000]
eb=list() #This is a variable used for storing elements
tib=list() #this variable is used for storing time


for m in range(0,len(rangee)):
    Ab = []    
    for l in range(0,rangee[m]):
        n = round(random.uniform(0,1),6)
        Ab.append(n) 
    start_timeb= time.time()
    bucketSort(Ab)
    end_timeb=time.time()
    total_timeb=end_timeb - start_timeb
    #print("Sorted array is:")
    #print(Ab)
    print(len(Ab), "Bucket sort for random floating numbers in range 0 to 1 is executed in ", + total_timeb, "sec")
    eb.append(len(Ab))
    tib.append(total_timeb)
    
    
    
    
#quick sort
def quickSort(A, p, r):
    if len(A) == 1:
        return A
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)       
def partition(A, p, r):
    x = A[r]  
    i = (p - 1)   # Boundary to Left/right element
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1                 # increment i
            A[i], A[j] = A[j], A[i]   # Swapping if the if condition is a satisfisfied.

    A[i + 1], A[r] = A[r], A[i + 1]   # Swapping
    return i + 1     # This is the q value


rangee=[10,100,1000,10000,100000]
e=list() #This is a variable used for storing elements
ti=list() #this variable is used for storing time

for x in range(0,len(rangee)):
    Aq=[]
    for y in range(0,rangee[x]):
        n = round(random.uniform(0,1),6)
        Aq.append(n) 
    n=len(Aq)
    start_time= time.time()
    quickSort(Aq,0,n-1)
    end_time=time.time()
    total_time=end_time - start_time
    #print("Sorted array is:")
    #print(Aq)
    print(len(Aq), "Quick sort for random floating numbers in range 0 to 1 is executed in ", + total_time, "sec")
    e.append(len(Aq))
    ti.append(total_time)

    

fig=plt.figure(figsize= (10,5))
plt.plot(eb,tib,label='actual time taken for bucket sort algorithm')
plt.plot(e,ti,label='actual time taken for quick sort algorithm')
plt.xlabel('Number of values in an array')
plt.xscale("log", base=10)
plt.ylabel('Actual Time spent by the algorithms')
plt.grid()
plt.legend()










# # Comparision of radix sort and  quick sort

# In[2]:


import time
import numpy as np
import matplotlib.pyplot as plt
import random



#Quick Sort
def quickSort(A, p, r):
    if len(A) == 1:
        return A
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)       
def partition(A, p, r):
    x = A[r]  
    i = (p - 1)   # Boundary to Left/right element
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1                 # increment i
            A[i], A[j] = A[j], A[i]   # Swapping if the if condition is a satisfisfied.

    A[i + 1], A[r] = A[r], A[i + 1]   # Swapping
    return i + 1     # This is the q value

e=list() #This is a variable used for storing elements
ti=list() #this variable is used for storing time
for l in range (1,6):
    A = np.random.randint(1, 1000, size=pow(10, l))
    n=len(A)
    start_time= time.time()
    quickSort(A,0,n-1)
    end_time=time.time()
    total_time=end_time - start_time
    #print("Sorted array is:")
    #print(A)
    print(len(A), "Quick sort for random integers is executed in ", + total_time, "sec")
    e.append(len(A))
    ti.append(total_time)

    
    
    
#Radix sort

def countingSort(A,pos):
    n=len(A) #this is the length of the array
    B=[0]*n #this is the final output array named B initializing with 0 and having the same size as the input array.
    C=[0]*10 #This is the C array(counting array), its size is as the no of digits in number system is 10(0-9) and is initialized with 0.
    
    #For storing the count of integers.
    for i in range(0,n):
        C[(A[i]//pos)%10] +=1
    
    #For cumulative sum of C array.
    for i in range(1,10):
        C[i]=C[i]+C[i-1]
      
    #The output array B is being built.
    i=n-1
    while i>=0:
        B[C[(A[i]//pos)%10]-1]=A[i]
        C[(A[i]//pos)%10]-=1
        i=i-1
    
    #copying the elements from output array B to A.
    for k in range(0,n):
        A[k]=B[k]



def radixSort(A):
    maximum=max(A) # get the maximum value of the total array
    pos=1 #This the position of the digit
    #Applying counting sort for every digits place like one's, ten's,..
    while (maximum/pos)>0:
        countingSort(A,pos)
        pos=pos*10
        

        
rangee=[10,100,1000,10000,100000]
er=list() #This is a variable used for storing elements
tir=list() #this variable is used for storing time
for i in range(0,len(rangee)):
    Ar = []
    for j in range(0,rangee[i]):
        n1 = random.randint(1,1000)
        Ar.append(n1)       
    start_timer= time.time()
    radixSort(Ar)
    end_timer=time.time()
    total_timer=end_timer - start_timer
    #print("Sorted array is:")
    #print(Ar)
    print(len(Ar), "radix sort for random integers is executed in ", + total_timer, "sec")
    er.append(len(Ar))
    tir.append(total_timer)

    
    

    
fig=plt.figure(figsize= (10,5))
plt.plot(er,tir, label='actual time taken for radix sort algorithm')

plt.plot(e,ti,label='actual time taken for quick sort algorithm')

plt.xlabel('Number of values in an array')
plt.xscale("log", base=10)
plt.ylabel('Actual Time spent by the algorithms')
plt.grid()
plt.legend()

