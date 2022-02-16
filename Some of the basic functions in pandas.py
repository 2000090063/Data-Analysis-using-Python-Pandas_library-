#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
df=pd.read_csv('football.csv')    #Reading a csv file and creating a data frame 
df                                #printing data frame object


# In[3]:


df['Neymar'][df['Primary Skill']=='Shooting']   #printing records using conditions


# In[3]:


r,c=df.shape                #priting shape of the data frame
print(r)
print(c)


# In[46]:


df['Neymar'].mean()   #using  math functions on columns


# In[4]:


df.head()       #displays first five records


# In[48]:


df.head(2)   #displays first 2 records(argument is passed as no of records)


# In[49]:


df.tail()


# In[50]:


df.tail(2)


# In[52]:


df[2:5]  #slicing the dta frames


# In[53]:


df[:]    


# In[54]:


df[::-1]                 #printing reverse of the data frame


# In[55]:


df.columns     #printing all the columns


# In[57]:


df.Neymar


# In[58]:


df['Neymar']#df.Neymar also we can use


# In[59]:


type(df['Neymar']) #printing type of the column


# In[69]:


df[['Secondary Skill','Lionel Messi','Christiano Ronaldo']] [df['Primary Skill']=='Shooting']


# In[84]:


df['Neymar'][df['Lionel Messi']==df['Lionel Messi'].max()]


# In[85]:


df[['Neymar','Primary Skill']][df['Lionel Messi']==df['Lionel Messi'].max()]


# In[86]:


df.tail()       #prints last five records of the data frame


# In[94]:


df.set_index('Primary Skill',inplace=True)


# In[95]:


df


# In[96]:


df.loc['Shooting']


# In[97]:


df.loc['Passing']        #printing records using loc fun 


# In[98]:


df.reset_index(inplace=True)      #resetting the index for data frame


# In[99]:


df


# In[6]:


df['Neymar']           #printing with column name


# In[ ]:




