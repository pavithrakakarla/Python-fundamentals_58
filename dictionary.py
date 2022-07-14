#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Introduction to dictionary :


# In[ ]:


definition : A dictionary is a combination of key value pairs.
    
classification : It is classified as an mutable datatype.

how to define or declare a dictionary datatype---------->{}

short form : dict


# In[ ]:


Note : dictioanary is extremely important interms of interview as well as it is extensively used datatype among all other
datatypes in realtime.


# In[1]:


alien = {'color':'green','points':5}


# In[2]:


print(alien)


# In[3]:


type(alien)


# ### Accessing the key value pairs in a dict :

# In[4]:


#req: I want to know the color of alien?

print(alien['color']) # give the key and get the value


# In[5]:


print(alien['points'])


# In[6]:


# req : can we give the value and get key value from dict?
print(alien['green'])


# NOTE : By using value, we cannot get the key, it is one way only. We can get value by using key of a dictionary

# ### Adding new key value pairs to the dictionary:

# In[7]:


print(alien)


# In[8]:


# Req : To add start_position=0 to the dictionary alien:

alien['start_position'] = 0


# In[9]:


print(alien)


# ### Changing values of keys in dict :

# In[10]:


# req : to change the color of alien from green to yellow:
alien['color'] = 'yellow'


# In[11]:


print(alien)


# ### Deleting key value pairs from dict : 

# In[12]:


# I want to delete key value pair from dict:

del alien['points']


# In[13]:


print(alien)


# ## Realtime usage of a dict :

# In[ ]:


#req : create an account in instagram :


# In[14]:


useraccount = {'username':'pythontraining', 'firstname':'python','lastname':'training','dob':'01-01-2020','pwd':'12345'}


# In[15]:


print(useraccount)


# In[ ]:





# In[ ]:





# In[ ]:




