
# coding: utf-8

# In[1]:


# forever whatever


# In[5]:


try: c
except NameError: c = __import__('traitlets').config.Config()


# In[6]:


from nbd import reads

with open('config/index.ipynb') as f:
    data = reads(f.read(), 4)


# In[4]:


def report():
    yield 'index', data

## A simple index.

from nbd import index
c.FilesWriter.build_directory = 'docs'
c.Docs.update(
    report=report,
    post=index(data, "h1,h2"))


# In[ ]:




