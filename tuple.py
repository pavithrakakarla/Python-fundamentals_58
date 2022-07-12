#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Introduction to tuple datatype :


# In[ ]:


Definition : An immutable list is called as a tuple.

Classification : It is classified as an immutable object.

How to define the tuple datatype ---------- ()


# In[2]:


numbers = (1,2,3,4,5)


# In[3]:


print(numbers)


# In[4]:


type(numbers)


# In[6]:


# req : I want to modify the number 3 to 8

numbers[2] = 8


# Note : We cannot change the data in same tuple. But we can redifine that with different data.
# Please find below example for reference.

# In[10]:


dimentions = (10,20) # I want to change 10 to 30. For this we need to redefine this tuple with 30,20.
print(dimentions)


# In[11]:


dimentions = (30,20)
print(dimentions)


# NOTE : We can fetch the data from tuple datatype. Apart from update on same variable, we can do all activities with tuple, what we can do with list.

# In[12]:


students = ('aditi', 'balu','candy','dolly')


# In[13]:


type(students)


# In[14]:


print(students[1])


# In[15]:


print(students[1].title())


# In[16]:


for i in students:
    print(i)


# ## dictionary datatype : dict()

# In[ ]:


Introduction to dictionary :


# In[ ]:


definition : A dictionary is a combination of key value pairs.
    
classification : It is classified as an mutable datatype.

how to define the dictionary datatype---------->{}

short form it is written as dict


# In[17]:


colors = { 'one':'green','two':'yellow', 'red':3}


# In[18]:


print(colors)


# In[19]:


type(colors)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




