# Determines if an object is iterable

## This function uses a couple of different methods to find out if a variable is iterable

```python
$pip install isiter
from isiter import isiter

from collections import namedtuple
fields_cor = "qt rgb r g b"
classname_cor = "cor"
Colorinfos = namedtuple(classname_cor, fields_cor)
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

html = """
<div class="div1">
<p>hello</p>
<p>hi</p>
    <div class="nesteddiv">
        <p>one</p>
        <p>two</p>
        <p>three</p>
    </div>
</div>
"""

print(f"""{isiter({1:2,3:2}, )=}""")
print(f"""{isiter([1,2,34], )=}""")
print(f"""{isiter((1,2,34), )=}""")
print(f"""{isiter(Colorinfos(1,2,34,3,3), )=}""")
print(f"""{isiter(sorted((1,2,34,3,3)), )=}""")
print(f"""{isiter(({1, 2, 34, 3, 3}), )=}""")
print(f"""{isiter((55), )=}""")
print(f"""{isiter((55.44), )=}""")
print(f"""{isiter((True), )=}""")
print(f"""{isiter((3.14 + 2.71j), )=}""")
print(f"""{isiter((pd.DataFrame([[3,3,3],[3,3,3]])), )=}""")
print(f"""{isiter((pd.Series([[3,3,3]])), )=}""")
print(f"""{isiter((np.array([[3,3,3]])), )=}""")
print(f"""{isiter((np.ndarray([3,3,3])), )=}""")
print(f"""{isiter((pd.NA), )=}""")
print(f"""{isiter((np.nan), )=}""")
print(f"""{isiter(BeautifulSoup(html, 'lxml'), )=}""")
print(f"""{isiter(bytearray(b'dgfasds'), )=}""")
print(
    f"""{isiter(bytearray(b'dgfasds'),consider_non_iter=(str, bytes, bytearray) )=}"""
)
print(f"""{isiter(b'bababa', )=}""")
print(f"""{isiter(b'bababa',consider_non_iter=(str, bytes, bytearray) )=}""")
print(f"""{isiter('str1', )=}""")
print(f"""{isiter('str2',consider_non_iter=(str, bytes, bytearray))=}""")



{1: 2, 3: 2} in (list, tuple, set, frozenset, dict)
isiter({1:2,3:2}, )=True
[1, 2, 34] in (list, tuple, set, frozenset, dict)
isiter([1,2,34], )=True
(1, 2, 34) in (list, tuple, set, frozenset, dict)
isiter((1,2,34), )=True
cor(qt=1, rgb=2, r=3 in (list, tuple, set, frozenset, dict)
isiter(Colorinfos(1,2,34,3,3), )=True
[1, 2, 3, 3, 34] in (list, tuple, set, frozenset, dict)
isiter(sorted((1,2,34,3,3)), )=True
{1, 2, 3, 34} in (list, tuple, set, frozenset, dict)
isiter(({1, 2, 34, 3, 3}), )=True
55 in (int, float, bool, complex, type(None))
isiter((55), )=False
55.44 in (int, float, bool, complex, type(None))
isiter((55.44), )=False
True in (int, float, bool, complex, type(None))
isiter((True), )=False
(3.14+2.71j) in (int, float, bool, complex, type(None))
isiter((3.14 + 2.71j), )=False
   0  1  2
0  3  3   == Iterable
isiter((pd.DataFrame([[3,3,3],[3,3,3]])), )=True
0    [3, 3, 3]
dtype == Iterable
isiter((pd.Series([[3,3,3]])), )=True
array([[3, 3, 3]]) == Iterable
isiter((np.array([[3,3,3]])), )=True
array([[[6.23042070e == Iterable
isiter((np.ndarray([3,3,3])), )=True
<NA> not iter
isiter((pd.NA), )=False
nan in (int, float, bool, complex, type(None))
isiter((np.nan), )=False
<html><body><div cla == Iterable
isiter(BeautifulSoup(html, 'lxml'), )=True
bytearray(b'dgfasds' == Iterable
isiter(bytearray(b'dgfasds'), )=True
bytearray(b'dgfasds' in (<class 'str'>, <class 'bytes'>, <class 'bytearray'>)
isiter(bytearray(b'dgfasds'),consider_non_iter=(str, bytes, bytearray) )=False
b'bababa' == Iterable
isiter(b'bababa', )=True
b'bababa' in (<class 'str'>, <class 'bytes'>, <class 'bytearray'>)
isiter(b'bababa',consider_non_iter=(str, bytes, bytearray) )=False
'str1' == Iterable
isiter('str1', )=True
'str2' in (<class 'str'>, <class 'bytes'>, <class 'bytearray'>)
isiter('str2',consider_non_iter=(str, bytes, bytearray))=False
```
