#!/usr/bin/env python
# coding: utf-8

# 1- [1pt] Import the Python modules you will need for this homework.

# In[2]:


### STUDENT ANSWER
# import relevant packages
import numpy as np
import nibabel


# 2\. [3pts] Basic Data Types
# - **(a)** Divide 6 by 2 using floating point division. Store this value in the name `a`. Then divide 6 by 2 using integer division. Store this value in the name `b`. Print both values.

# In[3]:


a = 6 / 2
b = 6 // 2

print(a)
print(b)


# In[4]:


# This checks whether you have created the names a and b, it does not check the result
ok.grade("q1_2a")


# In[5]:


# This is for later, when the homework is graded. Leave it commented out until then.
# ok.grade("q1_2a_full")


# - **(b)** Store the floating point value `5.0` into a name called `f`. Store the integer value `5` into a name called `i`. Divide `f` by `i`, store that in `f_divide_i` and print the type

# In[6]:


f = 5.0
i = 5
f_divide_i = f/i
print(type(f_divide_i))


# In[7]:


# To check whether your answer contains the right names
ok.grade("q1_2b")


# In[8]:


# For after grading
# ok.grade("q1_2b_full")


# - **(c)** Create the string `"5"` and store it in a name called `s`. Then multiply `s` by `i`, store the result in `si` and print out the result.

# In[9]:


s = "5"
si = s * i
print(si)


# In[10]:


# To check whether your answer contains the right names
ok.grade("q1_2c")


# In[11]:


# For after grading
# ok.grade("q1_2c_full")


# 3- [2pts] Lists and Tuples
# - **(a)** Create a tuple that contains each words of the following sentence as a separate object: `I love data science`. Store this tuple in a name called `tup`.

# In[12]:


tup = ('I', 'love', 'data', 'science')
print(tup)


# In[13]:


# To check whether your answer contains the right names
ok.grade("q1_3a")


# In[14]:


# For after grading
# ok.grade("q1_3a_full")


# - **(b)** Create an empty list and store it in a name called `l`. Then append `tup`, append another empty list, and append the number `5`. Finally print out this list.

# In[15]:


l = []
l.append(tup)
l.append([])
l.append(5)
print(l)


# In[16]:


# To check whether your answer contains the right names
ok.grade("q1_3b")


# In[17]:


# For after grading
# ok.grade("q1_3b_full")


# 4- [3pts] Creating Arrays
# - **(a)** Create a 1-d array that is a sequence of even numbers between 50 and 100, inclusive. Store this in a name called `seq_50_100` and print it out.

# In[18]:


seq_50_100 = np.arange(50, 101, 2)
print(seq_50_100)


# In[19]:


# To check whether your answer contains the right names
ok.grade("q1_4a")


# In[20]:


# For after grading
# ok.grade("q1_4a_full")


# - **(b)** Create another sequence that goes from `0.50` to `1.00` inclusive in increments of `0.02`. Store this in a name called `seq_half_one` and print it. **HINT** There is a quick way of doing this using a name you've already created.

# In[21]:


seq_half_one = seq_50_100 / 100
seq_half_one = np.arange(0.5, 1.01, .02)


# In[22]:


# To check whether your answer contains the right names
ok.grade("q1_4b")


# In[23]:


# For after grading
# ok.grade("q1_4b_full")


# In[24]:


seq_half_one[-1]


# - **(c)** Create a 3-D array of integers that all have the value `1`. Make it size `4 x 5 x 3` and store it in a name called `array_3d`, then print out its shape

# In[25]:


array_3d = np.ones((4,5,3), dtype=np.int)
print(array_3d.shape)


# In[26]:


# To check whether your answer contains the right names
ok.grade("q1_4c")

