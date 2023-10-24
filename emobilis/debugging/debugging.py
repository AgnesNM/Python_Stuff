#!/usr/bin/env python
# coding: utf-8

# In[5]:


#using print

#print("hello")


# def add(nums):
    
#     for num in nums:
#         print("debugging!")
#         if num<1:
#             print("debugging 1")
#             print("oops!")           
                        
#     return num  

# add([1,2,3,4])

def add(nums):
    
    for num in nums:
        #get to know what's going on in the 
        import pdb
        pdb.set_trace()
        if num<1:
            print("debugging 1")
            print("oops!")           
                        
    return num  

add([1,2,3,4])


# In[ ]:





