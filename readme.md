

```python
!jupyter nbconvert --to markdown readme.ipynb
!jupyter nbconvert --to python config/config.ipynb
!jupyter nbd --config config/config.py posts/**.ipynb
```

    [NbConvertApp] Converting notebook readme.ipynb to markdown
    [NbConvertApp] Writing 677 bytes to readme.md
    [NbConvertApp] Converting notebook config/config.ipynb to python
    [NbConvertApp] Writing 533 bytes to config/config.py
    Traceback (most recent call last):
      File "/Users/tonyfast/anaconda/bin/jupyter-nbd", line 11, in <module>
        load_entry_point('nbd', 'console_scripts', 'jupyter-nbd')()
      File "/Users/tonyfast/anaconda/lib/python3.5/site-packages/setuptools-27.2.0-py3.5.egg/pkg_resources/__init__.py", line 565, in load_entry_point
      File "/Users/tonyfast/anaconda/lib/python3.5/site-packages/setuptools-27.2.0-py3.5.egg/pkg_resources/__init__.py", line 2598, in load_entry_point
      File "/Users/tonyfast/anaconda/lib/python3.5/site-packages/setuptools-27.2.0-py3.5.egg/pkg_resources/__init__.py", line 2258, in load
      File "/Users/tonyfast/anaconda/lib/python3.5/site-packages/setuptools-27.2.0-py3.5.egg/pkg_resources/__init__.py", line 2264, in resolve
      File "/Users/tonyfast/nbd/nbd.py", line 48, in <module>
        def identity(path, resources: dict=None, **kw) -> t.Tuple[NotebookNode, dict]:
    NameError: name 't' is not defined

