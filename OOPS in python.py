#!/usr/bin/env python
# coding: utf-8

# # OOPS in Python

# In[17]:


class Car:
    def __init__(self,window,door,engine):
        self.window=window
        self.door=door
        self.engine=engine 
    def self_driving(self):
        if self.engine == "petrol":
            print("This is a {} car".format(self.engine))
        elif self.engine == "Diesel":
            print("This is a {} car".format(self.engine))
        else:
            print("This car is a self driving car")
        
##self is a refernce to a particular object


# In[18]:


car=Car(4,4,"petrol")


# In[19]:


car.window


# In[20]:


car2=Car(2,3,"Diesel")
car2.door


# In[21]:


car2.engine


# In[22]:


car.self_driving()


# In[23]:


car2.self_driving()


# In[26]:


car3=Car(2,3,"Electric")


# In[27]:


car3.self_driving()


# In[6]:


dir(Car)


# In[ ]:





# In[ ]:




