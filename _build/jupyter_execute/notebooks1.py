#!/usr/bin/env python
# coding: utf-8

# # Part 1b - Jupyter Notebooks
# 
# In this assignment, each Jupyter (.ipynb) file needs to contain at least
# 
# - 5 Markdown cells with a total of at least
#     - 2 block math equations
#     - 2 code blocks
#     - 2 image files
# - 5 executable code cells
# - 2 plots generated using 2 (additional) hidden code cells
# 

# ## Markdown cell of a Math Equation
# 
# $$ 1 + 1 = 2$$
# $$ 2 + 2 = 4$$
# 
# When writing the LaTeX above, I learned that there needs to be spaces between each character.

# ## Code Blocks
# Notebooks can also hold code blocks. Examples adapted from "Introduction to Systematic Program Design in Python" by UBC Extended Learning
# 
# ```{figure} https://a.storyblok.com/f/128630/357x81/2d5985e091/ubc-logo-ext-learning-white-bg.png
# ---
# height: 50px
# name: EL-logo
# ---
# ```
# 
# ```{figure} https://d3njjcbhbojbot.cloudfront.net/api/utilities/v1/imageproxy/https://coursera-course-photos.s3.amazonaws.com/37/6352a069b511e3ae92c39913bb30e0/DataScientistsToolbox.jpg?auto=format%2Ccompress&dpr=1
# ---
# height: 100px
# name: DataScienceToolbox-logo
# ---
# ```

# In[1]:


sum = 0

list_of_numbers = [4, 9, 1]

for n in list_of_numbers:
    sum = sum + n
sum


# In[2]:


sum = 0

list_of_large_numbers = [4444, 9999, 1111]

for n in list_of_large_numbers:
    sum = sum + n
sum


# ## Charts from hidden code cells

# In[3]:


import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(2,15)
fig, ax = plt.subplots()
ax.scatter(*data, c=data[1], s=100*np.abs(data[0]));


# In[4]:


data = np.random.randn(2,75)
fig, ax = plt.subplots()
ax.scatter(*data, c=data[1], s=50*np.abs(data[0]));

