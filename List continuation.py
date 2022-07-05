#!/usr/bin/env python
# coding: utf-8

# ### Organizing the list datatype

# In[1]:


cars = ['maruthi','bmw','audi','benz','volvo','suzuki']


# In[2]:


print(cars)


# ## sorting the list:
# 
# #### 1. sorted()------->temperory approach--------->we will bw able to get the original order of the list declared.
# #### 2. sort()----------> perminent approach--------->changes will be applied perminently and we will not be able to get the original order back.

# #### 1.sorted() method

# In[3]:


print(sorted(cars))  #a-z


# In[5]:


print(cars)   # orignal still exists in this sorted method


# #### 2. sort() method

# In[6]:


cars.sort()


# In[7]:


print(cars) #changes perminently applied in sort method


# ### list reverse order:
# #### reverse()

# In[8]:


print(cars)


# In[9]:


cars.reverse()


# In[10]:


print(cars)


# ### counting no. of elements in the list:
# #### len()

# In[11]:


print(cars)


# In[12]:


len(cars)


# ## slicing the list datatype
# 
# #### general syntax of slicing :  [start value : stop value : step count]
# 
# #### NOTE : stop value is always exclusive, to include it we have to increment the index by +1.

# In[13]:


sections = ['a','b','c','d','e','f']


# In[16]:


# I want to include 'b' and 'd' in one slice.
print(sections[1:4:2])


# In[25]:


# I want to include 'a' and 'e' in one slice.
print(sections[0:5:4])


# In[26]:


# I want to include 'c' and 'f' in one slice.
print(sections[2:6:3])


# In[27]:


# I want to include 'a''c','e' in one slice.
print(sections[0:5:2])


# In[ ]:




