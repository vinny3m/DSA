#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Binary search tree finding the successor when a key is given.


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def findSucc(root, key):
    if root is None:
        return
    #when the key is present at root
    if root.key == key:
        if root.right is not None:
            tmp = root.right
            while(temp.left):
                tmp = tmp.left
            findSucc.suc = tmp
 
        return
    # Checking whether the key is smaller than the root and traversing towards left side
    if root.key > key :
        findSucc.suc = root
        findSucc(root.left, key)
 
    else:       
        findSucc(root.right, key)

        
def insert(node , key):
    if node is None:
        return Node(key)
 
    if key < node.key:
        node.left = insert(node.left, key)
 
    else:
        node.right = insert(node.right, key)
 
    return node





root = None
root = insert(root, 3)
insert(root, 4);
insert(root, 0);
insert(root, 8);
insert(root, 2);
insert(root, 10);
insert(root, 5);


findSucc.suc = None

key = 6 #This is the key value needed to be searched
findSucc(root, key)



if findSucc.suc is not None:
    print ("The Successor is", findSucc.suc.key)
else:
    print ("There is no Successor")

