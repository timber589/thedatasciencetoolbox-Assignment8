#!/usr/bin/env python
# coding: utf-8

# # Part 2a - Summary of the Course
# 
# ## Course Summary
# The information below represents a summary of the content of the course, "The Data Science Toolbox" in the Fall of 2022 with Course Facilitators:  Analise Hofmann (Email: analise.hofmann@ubc.ca) and Matt Connell (Email: matthew.connell@ubc.ca)

# ### Module 1 - Introduction to the Data Science Toolbox
# 
# 1. Explain why it is important to use the right tool for the job.
# 2. Name the tools in the data science toolbox and explain their main purposes.
# 3. Describe the different components of the JupyterLab interface.
# 4. Ask effective questions.
# 5. Create minimal reproducible code examples when asking for help

# ### Module 2 - The Shell
# ```{figure} https://s3.us-west-2.amazonaws.com/secure.notion-static.com/67be5b97-7a01-4cda-82c4-2a071ed1fccd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221212T045957Z&X-Amz-Expires=86400&X-Amz-Signature=f1108f036b6017467c41a777650e7b326abf5c803272f7be966ab2b97bdcf903&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject
# ---
# height: 200px
# name: bash-logo
# ---
# ```
# 
# 1. Use the shell to navigate the computer’s filesystem
# 2. Create new files and directories
# 3. Move, copy, and delete files and directories
# 4. Use "wildcards"
# 5. Define and distinguish between absolute file paths and relative file paths
# 6. Read the shell's built-in manual
# 7. Combine commands with pipes

# ### Module 3 - Git and GitHub intro
# 
# ```{figure} https://s3.us-west-2.amazonaws.com/secure.notion-static.com/cedaa456-d92d-4a9d-bbf4-3cf946c7e92e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221212T050116Z&X-Amz-Expires=86400&X-Amz-Signature=a5e99b41acdc8d047a87c1ee16e2b3c9007c8fb0cce8a81c2155010ce89c8b29&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject
# ---
# height: 200px
# name: Git-Github-logo
# ---
# ```
# 
# 1. Differentiate between the use of GitHub as a remote hosting service for version control and Git as a version control system.
# 2. Identify a Git repository.
# 3. Implement Git's `clone`, `add`, `status`, `commit`, `pull`, and `push` operations on the command line and their equivalent use in the JupyterLab IDE.
# 4. Understand what it implies to use the staging area in a Git workflow.
# 5. Use commits as the primary building block for storing a project versions together with an attached message and a unique identifier.

# ### Module 4 - Getting groovy with Git and GitHub
# 
# 1. Explore the Git history via **`git log`** in the terminal, and the equivalent functions in JupyterLab and GitHub.
# 2. Compare commits using **`git diff`** in the terminal, and the equivalent functions in JupyterLab and GitHub.
# 3. Solve merge conflicts at the command line and in VS Code.
# 4. Avoid pushing certain local files by including a **`.gitignore`** file.
# 5. Differentiate between doing a revert and a hard reset of a commit when restoring an older version of a project.

# ### Module 5 - Branches, forks, and streams… Welcome to the Git nature walk
# 
# 1. Manage feature-based development efficiently with Git in JupyterLab and in the terminal.
# 2. Infer a repository's current status and collaboration pattern by looking at visualizations of the project history in VS Code.
# 3. Differentiate when to use forking or branching as a collaboration strategy.
# 4. Recognize the essential components of a pull request.
# 5. Determine whether directly merging changes is preferable to first opening a pull request.
# 6. Explain when GitHub issues are helpful and how to use them.

# ### Module 6 - File Names, Project Organization, Virtual Environments
# 
# 1. Name files in a human- and machine-readable manner.
# 2. Organize projects with a meaningful folder hierarchy.
# 3. Install packages using the **`conda`** package manager.
# 4. Manage virtual environments with **`conda`** to keep track of project-specific package versions.

# ### Module 7 - Jupyter Lab
# 
# ```{figure} https://s3.us-west-2.amazonaws.com/secure.notion-static.com/15b2ab7f-ba1a-4a2a-b096-58bd3794d7b0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221212T050216Z&X-Amz-Expires=86400&X-Amz-Signature=4d9d212cf6d9f277834b21e5b3fd63387ceb9cae409f5c99d1dcdb9cb4778f21&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject
# ---
# height: 200px
# name: jupyterlab-logo
# ---
# ```
# 
# 1. Perform literate data science programming using Jupyter Notebooks.
# 2. Use Markdown to efficiently produce formatted text.
#     Includes writing math formulas inline with the text by writing two `$$` before and after LATEX code. Example: $ pi + 1 = 4.14 $
# 3. Enhance productivity via advanced JupyterLab features.
#     Magic Commands includes `%hist`, `%reset`, `%%timeit` (example below), `%debug` that were discussed in the course.
# 4. Export notebooks to various formats for sharing your work.

# In[1]:


get_ipython().run_cell_magic('timeit', '', 'for i in range(1_000_000):\n    (i - 0.1)**2\n')


# ### Module 8 - Jupyter Book
# 
# ```{figure} https://s3.us-west-2.amazonaws.com/secure.notion-static.com/615f68bd-7484-4ecd-81b3-b8ad9f4a522f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221212T050301Z&X-Amz-Expires=86400&X-Amz-Signature=af29a8b4b5a769de89dd4d363dc4b2062949ddd5d44b3c2ea76256ba5b3b8003&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject
# ---
# height: 200px
# name: jupyterbook-logo
# ---
# ```
# 
# 1. Explain the Jupyter Book ecosystem.
# 2. Build Jupyter Books via the command line.
# 3. Create your own content files.
#     Content includes showing and hiding code and its output (examples of charts below)
# 4. Publish your book online for free using GitHub Pages.

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
data = np.random.randn(2,750)
fig, ax = plt.subplots()
ax.scatter(*data, c=data[1], s=500*np.abs(data[0]));


# In[3]:


data = np.random.randn(2,3)
fig, ax = plt.subplots()
ax.scatter(*data, c=data[1], s=5*np.abs(data[0]));

