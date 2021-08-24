#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


inpt = np.logspace(0,15,1000) 
inpt


# In[3]:


g_1 = np.ones(1000)
g_n = inpt
g_square = inpt*inpt
g_squareroot = np.sqrt(inpt)
g_nlogn = inpt*np.log(inpt)
g_cube = inpt**3
g_2n = 2**inpt


# In[4]:


figure = plt.figure()
t = figure.add_subplot(1,1,1)
t.set_yscale('log')
t.set_xscale('log')
t.set_xlim(1,10**15)
t.set_ylim(1,10**19)
t.plot(inpt,g_1,label='1')
t.plot(inpt,g_n,label='n')
t.plot(inpt,g_square,label='n*n')
t.plot(inpt,g_squareroot,label='sqrt(x)')
t.plot(inpt,g_nlogn,label='nlog(n)')
t.plot(inpt,g_cube,label='n^3')
t.plot(inpt,g_2n,label='2^n')
plt.legend()


# In[ ]:




