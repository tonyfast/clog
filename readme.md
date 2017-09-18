
# clog


```python
from IPython.display import *; from pathlib import Path
for path in Path('.').rglob('*.ipynb'): 'checkpoints' not in str(path) and display(Markdown("[{}]()".format(path)))
```


[config.ipynb]()



[readme.ipynb]()



[clog/2017-09-10-Project-Statistics.ipynb]()



[clog/2017-09-11-Gaskets-in-a-storm.ipynb]()



[clog/2017-09-12-Atlanta-Wages.ipynb]()



[clog/2017-09-14-About-Me.ipynb]()



```python
!jupyter nbconvert --to markdown readme.ipynb
```
