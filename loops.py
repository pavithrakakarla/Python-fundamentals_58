#!/usr/bin/env python
# coding: utf-8

# ## Introduction to looping statements:

# In[ ]:





# In[4]:


students = ['kalyan', 'latha','naren','faisal','laxmi','haritha']


# In[5]:


students


# In[6]:


print(students)


# In[7]:


type(students)


# ##### req: i want to appreciatee all students

# In[12]:


message = f'keep up the good work {students[0].title()}'

print(message)


# In[14]:


message = f'keep up the good work {students[5].title()}'

print(message)


# ### for loop:

# #### General syntax of a for loop

# In[ ]:


#formula for for loop:

for tempvar in mainvar:
    print(tempvar)


# In[16]:


#I want to appreciate all students at a time:

for x in students:
    print(f"keep up the good work, {x.title()}")          


# #### indentation:

# In[17]:


for i in students:
    print(i)


# In[18]:


for i in students:
print(i)


# In[19]:


# i want to add one more message to all students: like practice well.. and enjoy your work

for i in students:
    print(f'keep up the good work, {i.title()}')
    print(f'practice well.. and enjoy your work, {i.title()}')


# In[20]:


# new line space: \n
for i in students:
    print(f'keep up the good work, {i.title()}')
    print(f'practice well.. and enjoy your work, {i.title()}\n')


# In[22]:


# out of loop message:
#print() without indentation

for i in students:
    print(f'keep up the good work, {i.title()}')
    print(f'practice well.. and enjoy your work, {i.title()}\n')
    
print('thank you all') # writing out of loop


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




