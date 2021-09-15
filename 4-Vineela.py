#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Heap sort
def maxHeapify(A, n, i):    # n is the size of heap
    lar = i    # Initializing the largest
    l = 2 * i + 1   # This is the left child
    r = 2 * i + 2  # This is the right child

    # check whether the left child is bigger than parent
    if l < n and A[i] < A[l]:
        lar = l
    # check whether the right child is bigger than parent
    if r < n and A[lar] < A[r]:
        lar = r

    # Change the root
    if lar != i:
        A[i], A[lar] = A[lar], A[i]  # swap
        maxHeapify(A, n, lar)


# The main function to sort an array by heapSort
def heapSort(A):
    buildMaxHeap(A);
        
    n=len(A) #n is the size of the heap
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0] # swapping
        n=len(A) -1
        maxHeapify(A, i, 0)

def buildMaxHeap(A):
    n=len(A)
    for i in range(n // 2 , -1, -1):  # Floor division 
        maxHeapify(A, n, i)
        
A=[10,4,6,8,9,19,56,35,19]


heapSort(A)
print("The sorted array is :")
print(A) 


# In[2]:


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


A=[10,4,6,8,9,19,56,35,19]
n=len(A)
quickSort(A,0,n-1)
print("The sorted array is :")
print(A)


# In[3]:


#Compare between heap sort and quick sort algorithms using graphs
import time
import numpy as np
import matplotlib.pyplot as plt


def maxHeapify(A, n, i):    # n is the size of heap
    lar = i    # Initializing the largest
    l = 2 * i + 1   # This is the left child
    r = 2 * i + 2  # This is the right child

    # check whether the left child is bigger than parent
    if l < n and A[i] < A[l]:
        lar = l
    # check whether the right child is bigger than parent
    if r < n and A[lar] < A[r]:
        lar = r

    # Change the root
    if lar != i:
        A[i], A[lar] = A[lar], A[i]  # swap
        maxHeapify(A, n, lar)
# The main function to sort an array by heapSort
def heapSort(A):
    buildMaxHeap(A);
        
    n=len(A) #n is the size of the heap
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0] # swapping is done
        n=len(A) -1
        maxHeapify(A, i, 0)
def buildMaxHeap(A):
    n=len(A)
    for i in range(n // 2 , -1, -1):  # Floor division 
        maxHeapify(A, n, i)
        
ele=list() #This variable is used for storing elements
t=list() #This variable is used for storing time
for k in range (0,6):
    A = np.random.randint(-100, 1000, size=pow(10, k))
    start_t= time.time()   
    heapSort(A)
    end_t=time.time()
    total_t=end_t - start_t
    #print("Sorted array is:")
    #print(A)
    print(len(A), "Heap sort for random integers is executed in ", + total_t, "sec")
    ele.append(len(A))
    t.append(total_t)
    

    
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
for l in range (0,6):
    A = np.random.randint(-100, 1000, size=pow(10, l))
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

    
fig=plt.figure(figsize= (10,5))
plt.plot(ele,t, label='actual time taken for heap sort algorithm')

plt.plot(e,ti,label='actual time taken for quick sort algorithm')

plt.xlabel('Number of values in an array')
plt.xscale("log", base=10)
plt.ylabel('Actual Time spent by the algorithms')
plt.grid()
plt.legend()

