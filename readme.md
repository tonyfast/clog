

```python
!jupyter nbconvert --to markdown readme.ipynb
!jupyter nbconvert --to python config/config.ipynb
!jupyter nbd --config config/config.py posts/**.ipynb
```

    [NbConvertApp] Converting notebook readme.ipynb to markdown
    [NbConvertApp] Writing 1380 bytes to readme.md
    [NbConvertApp] Converting notebook config/config.ipynb to python
    [NbConvertApp] Writing 524 bytes to config/config.py
    [Docs] Converting notebook posts/2017-09-10-First-Post.ipynb to html
    [Docs] Writing 253471 bytes to docs/posts/2017-09-10-First-Post.ipynb.html
    [Docs] Converting notebook posts/2017-09-10-Project-Statistics.ipynb to html
    [Docs] Writing 290468 bytes to docs/posts/2017-09-10-Project-Statistics.ipynb.html
    [Docs] Converting notebook posts/2017-09-11-Gaskets-in-a-storm.ipynb to html
    [Docs] Writing 369862 bytes to docs/posts/2017-09-11-Gaskets-in-a-storm.ipynb.html
    [Docs] Converting notebook posts/jupyter4kids.ipynb to html
    [Docs] Writing 268436 bytes to docs/posts/jupyter4kids.ipynb.html
    [Docs] Converting notebook posts/powers-often.ipynb to html
    [Docs] Writing 250242 bytes to docs/posts/powers-often.ipynb.html
    [Docs] Converting notebook into html
    [Docs] Writing 251224 bytes to docs/index.html
    [Docs] Converting notebook into html
    [Docs] Writing 249240 bytes to docs/about.html

