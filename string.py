#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pwd', '')


# ### Continuation to strings:

# In[2]:


full_name = 'rahul ahrer'
print(full_name)


# In[3]:


print(full_name.title())


# In[4]:


#2. full name in capital letters

print(full_name.upper())


# In[5]:


#3. full name in small letters:

print(full_name.lower())


# ### f string:

# In[ ]:


# general syntax of a f string:

f" custom words {placeholder1} {placeholder2}........{placeholdern}


# In[6]:


first_name = 'rahul'
last_name = 'ahrer'


# In[7]:


# I want to get the full name at a time:

full_name = f" {first_name} {last_name}"
print(full_name)


# In[8]:


print(full_name.title())


# In[12]:


message = f" keep up the good work, {first_name} {last_name}"
print(message.title())


# In[13]:


message = f" keep up the good work, {full_name}"
print(message.title())


# In[14]:


message = f" keep up the good work, {full_name.title()}"
print(message)


# ### Adding white spaces to strings:
# 
# #### \n = new line delimeter
# 
# #### \t = tab delimeter

# In[19]:


print( "favourite_programming_language:pythoncjavac++reactjs")


# #### \n = next line delimeter

# In[20]:


# \n = next line delimeter

print( "favourite_programming_language:\npython\nc\njava\nc++\nreactjs")


# #### \t = tab delimeter

# In[22]:


#t = tab delimeter

print( "favourite_programming_language:\n\tpython\n\tc\n\tjava\n\tc++\n\treactjs")


# ### Removing white spaces from strings :
# 
# #### lstrip() = revong left side space
# #### rstrip() = removing right side space

# In[23]:


name = 'python'
print(name)


# In[ ]:


# lstrip() = revong left side space


# In[31]:


name2 = ' python'
print(name2)


# In[32]:


name2.lstrip()


# In[33]:


# rstrip() = removing right side space


# In[34]:


name3 = 'python '
print(name3)


# In[35]:


name3.rstrip()


# In[ ]:





# In[ ]:





# In[ ]:




