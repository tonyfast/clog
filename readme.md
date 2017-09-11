

```python
!jupyter nbconvert --to markdown readme.ipynb
!jupyter nbconvert --to python config/config.ipynb
!jupyter nbd --config config/config.py posts/**.ipynb
```

    [NbConvertApp] Converting notebook readme.ipynb to markdown
    [NbConvertApp] Writing 677 bytes to readme.md
    [NbConvertApp] Converting notebook config/config.ipynb to python
    [NbConvertApp] Writing 447 bytes to config/config.py
    [Docs] Converting notebook posts/2017-09-10-Project-Statistics.ipynb to html
    [Docs] Writing 342512 bytes to docs/posts/2017-09-10-Project-Statistics.ipynb.html
    [Docs] Converting notebook into html
    [Docs] Writing 250624 bytes to docs/index.html

