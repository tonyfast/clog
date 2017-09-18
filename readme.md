
# clog


```python
from IPython.display import *; from pathlib import Path
for path in Path('.').rglob('*.ipynb'): 'checkpoints' not in str(path) and display(
    Markdown("[{}]({})".format(path, path.with_suffix('.html'))))
```


[config.ipynb](config.html)



[readme.ipynb](readme.html)



[clog/2017-09-10-Project-Statistics.ipynb](clog/2017-09-10-Project-Statistics.html)



[clog/2017-09-11-Gaskets-in-a-storm.ipynb](clog/2017-09-11-Gaskets-in-a-storm.html)



[clog/2017-09-12-Atlanta-Wages.ipynb](clog/2017-09-12-Atlanta-Wages.html)



[clog/2017-09-14-About-Me.ipynb](clog/2017-09-14-About-Me.html)



```python
!jupyter nbconvert clog/*.ipynb && jupyter nbconvert --to markdown readme.ipynb
```

    [NbConvertApp] Converting notebook clog/2017-09-10-Project-Statistics.ipynb to html
    [NbConvertApp] Writing 286307 bytes to clog/2017-09-10-Project-Statistics.html
    [NbConvertApp] Converting notebook clog/2017-09-11-Gaskets-in-a-storm.ipynb to html
    [NbConvertApp] Writing 483346 bytes to clog/2017-09-11-Gaskets-in-a-storm.html
    [NbConvertApp] Converting notebook clog/2017-09-12-Atlanta-Wages.ipynb to html
    [NbConvertApp] Writing 320466 bytes to clog/2017-09-12-Atlanta-Wages.html
    [NbConvertApp] Converting notebook clog/2017-09-14-About-Me.ipynb to html
    [NbConvertApp] Writing 366415 bytes to clog/2017-09-14-About-Me.html
    [NbConvertApp] Converting notebook readme.ipynb to markdown
    [NbConvertApp] Writing 797 bytes to readme.md

