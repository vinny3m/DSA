#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Use stacks to check integrity of parenthesis

openn= ['{','[','(']
close= ['}',']',')']
mapp= dict(zip(openn,close)) #making a dictionary, to understand the corresponding pair of brackets
stack=[]
val=int(input("Enter no of input brakets given by the user:"))
for i in range(0,val):
    inp=input("Enter input as bracket:")
    if (inp in openn):
        stack.append(inp)
    elif (inp in close):
        key=list(mapp.keys())[list(mapp.values()).index(inp)]        
        if(stack[-1] == key): #checking if the peek value of the stack is equal to the key of closing bracket.
            stack.pop()       
    else:
        print("wrong input is given")

if (stack == []):
    print("okay")
else:
    print("not okay")
print(stack)


# In[ ]:




