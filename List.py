#!/usr/bin/env python
# coding: utf-8

# ## Introduction to list datatypes

# In[ ]:


Definition : A list is a selection of items listed in a particular order.
    
Classification : It is classified as a mutable datatype. ( flaxible -----> which we can edit  and alter)

How to declare a list?..... []


# #### Indexing of lists

# In[1]:


students = ['praveena','sandeep','sarada','venkat','hari','laxmi'] #Index : 0,1,2,3,4,5


# In[2]:


print(students)


# In[3]:


type(students)


# #### Accessing of elements in list by using indexing: 0,1,2,..

# In[5]:


# I want to access sandeep from list.

print(students[1])


# #### I want to add elements to the above list : append(), extend(), insert()

# In[ ]:


append(), extend(), insert()


# In[8]:


# I want to add sachin to the above list :
students.append('sachin')


# In[12]:


print(students)


# In[ ]:


# I want to add zaid to the 2nd index of above list


# In[20]:


students.insert(2,'zaid')


# In[21]:


students


# In[23]:


print(students[2])


# In[24]:


print(students[2].title())


# In[ ]:


get_ipython().set_next_input('Interview question : what is the difference between append and insert method in a list datatype');get_ipython().run_line_magic('pinfo', 'datatype')


# #### Modifying elaments from list:

# In[25]:


print(students)


# In[26]:


# I want to change hari name to iqbal
students[5] = 'iqbal'


# In[27]:


print(students)


# #### Deleting  elements from list:
# ##### pop()------->temporary delete
# ##### remove()
# ##### del -------->perminent delete

# In[28]:


#I want to delete sandeep name from list
del students[1]


# In[29]:


print(students)


# ##### temperory delete : pop()
# 
# pop() by default it will be deleting the last elements in the list and will be creating a carbon copy of the deleted items to the variable assigned to it.
# 

# In[30]:


x = students.pop()


# In[31]:


print(students)


# In[32]:


print(x)


# In[33]:


get_ipython().set_next_input('Interview question :  what is the difference between delete and pop methods of a list');get_ipython().run_line_magic('pinfo', 'list')


# In[ ]:




