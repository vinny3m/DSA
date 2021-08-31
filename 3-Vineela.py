#!/usr/bin/env python
# coding: utf-8

# ## MAXIMUM SUB ARRAY

# In[1]:


import time
import numpy as np
import matplotlib.pyplot as plt


def maxCrossingSubArray(array, lower, middle, higher):
    left_sum= -np.inf #initializinf the left sum value to be initially negative infinity value
    summ=0
    
    # this is for finding the max left sum value.
    for i in range (middle,lower-1,-1):
        summ=summ+array[i]
        if(summ > left_sum):
            left_sum=summ
            max_left=i
                     
    summ=0
    right_sum= -np.inf #initializinf the right sum value to be initially negative infinity value
    
    #This is for finding the maxing right sum value.
    for j in range (middle+1, higher+1):
        summ=summ+array[j]
        if(summ>right_sum):
            right_sum=summ
            max_right=j
    
    max_value=  (left_sum+right_sum )
    return (max_left, max_right, max_value)


def findMaxSubArray(array, lower, higher):
    if(lower==higher): # This is for base condition when there is only one element.
        return (lower,higher,array[lower])
    else: #If there are more than one elements then we do divide and conquer method
        mid = (lower+higher)//2
        #Now we find l, r,c values means left side sum, right side sum, and cross sum values
        (left_low, left_high, left_sum) = findMaxSubArray(array, lower, mid)
        (right_low,right_high,right_sum) = findMaxSubArray(array,mid+1,higher)
        (cross_low, cross_high, cross_sum) = maxCrossingSubArray(array,lower,mid,higher)
        
        # from all the three l,r,c values we select the max value either left sum, right sum or cross sum.
        if((left_sum >= right_sum)  and (left_sum >= cross_sum)):
            return (left_low,left_high, left_sum)
        elif((right_sum>= left_sum) and (right_sum>=cross_sum)):
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)
         
        
        
rangee=[10,100,1000,10000,100000,1000000] #considering many sizes of n
time_taken=[] # actual time taken for different sizes of inputs will be stored in this 
for k in range (0,len(rangee)):
    array=np.random.randint(-100,100,rangee[k])
    start_t=time.time()
    (low,high,sm) = findMaxSubArray(array, 0, len(array)-1) 
    time_e=time.time() -start_t #time difference between the start and end of algorithm for various values of size n in one iteration.
    time_taken.append(time_e) 
    print("t is ", time_taken)
    #In this time taken by the system to run differnt input sizes will be stored, in 1st iteration n is 10 
    #so time taken by the algo to give a solution for 10 numbers will be stored , same follows for all.
    
fig=plt.figure(figsize= (10,5))
plt.plot(rangee,time_taken, label='actual time')


#Hint: You need to convert complexity into the same scale as time, so you can compare it with actual performances. 
#To convert steps to time, you simply need to multiply with some c.   For example, instead of plotting n log n,
#you plot c * n log n.     For my choice, I use c = 1/500,000   
    
c=1/500000 #When the different c value is taken then the graph also changes as the y1 value changes

y1= c*(rangee*(np.log(rangee))) # c*nlogn gives us the theoritical time taken by the different sizes of n.
print("y1 is:", y1)
plt.plot(rangee,y1, label='theoritical time')
plt.xscale("log", base=10)
plt.ylabel('Time')
plt.legend()
    


# In[ ]:





# In[ ]:




