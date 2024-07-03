# No more sleepless nights due to a nested dict, json, list or whatsoever

#### A convenient way to handle nested iterables! Works only with Python 3.9 and up!

### Updates

**2022/09/30**: Fixed some problems with ProtectedDict and ProtectedList,ProtectedTuple

**2022/09/30**: Can be used as a generator now: **from flatten_any_dict_iterable_or_whatsoever import fla_tu**

**2022/09/30**: New functions: **get_from_original_iter**,**set_in_original_iter**, **create_random_dict**

**2022/09/30**: Added doc strings

## How to use the new functions **get_from_original_iter**,**set_in_original_iter**,

```python
data={'level1': {'t1': {'s1': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9},
                   's2': {'col1': 1, 'col2': 5, 'col3': 4, 'col4': 8},
                   's3': {'col1': 11, 'col2': 8, 'col3': 2, 'col4': 9},
                   's4': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9}},
                   ....]
list(fla_tu(data))

    [(5, ('level1', 't1', 's1', 'col1')),
     (4, ('level1', 't1', 's1', 'col2')),
     (4, ('level1', 't1', 's1', 'col3')),
     (9, ('level1', 't1', 's1', 'col4')),
     ....]

#After having flattened the iterable using fla_tu(), you will have a list of tuples:
#You can use now:

get_from_original_iter(iterable=data, keys=('level1', 't1', 's1', 'col1'))
Out[6]: 5
#to access the values.

set_in_original_iter(iterable=data, keys=('level1', 't1', 's1', 'col1'), value=1000000000000000000)
#to change values of the ORIGINAL ITERABLE!.


Out[8]:
{'level1': {'t1': {'s1': {'col1': 1000000000000000000,
    'col2': 4,
    'col3': 4,
    'col4': 9},
   's2': {'col1': 1, 'col2': 5, 'col3': 4, 'col4': 8},
   's3': {'col1': 11, 'col2': 8, 'col3': 2, 'col4': 9},
   's4': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9}},

THIS FUNCTION RETURNS >>>NONE<<<
BECAUSE IT CHANGES THE ORIGINAL ITERABLE!

    BE CAREFUL WHAT YOU ARE DOING!!

#DON'T USE data=set_in_original_iter(iterable=data, keys=('level1', 't1', 's1', 'col1'), value=1000000000000000000)


#If you still need the original data, use:

from copy import deepcopy
data2 = deepcopy(data)
list(fla_tu(data))
set_in_original_iter(iterable=data, keys=('level1', 't1', 's1', 'col1'), value=1000000000000000000)
data will be changed
data2 remains unchanged
```

```python
from flatten_any_dict_iterable_or_whatsoever import ProtectedList,ProtectedDict,ProtectedTuple
from flatten_any_dict_iterable_or_whatsoever import fla_tu

#without protection
data={'level1': {'t1': {'s1': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9},
                   's2': {'col1': 1, 'col2': 5, 'col3': 4, 'col4': 8},
                   's3': {'col1': 11, 'col2': 8, 'col3': 2, 'col4': 9},
                   's4': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9}},
            't2': {'s1': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9},
                   's2': {'col1': 1, 'col2': 5, 'col3': 4, 'col4': 8},
                   's3': {'col1': 11, 'col2': 8, 'col3': 2, 'col4': 9},
                   's4': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9}},
            't3': {'s1': {'col1': 1, 'col2': 2, 'col3': 3, 'col4': 4},
                   's2': {'col1': 5, 'col2': 6, 'col3': 7, 'col4': 8},
                   's3': {'col1': 9, 'col2': 10, 'col3': 11, 'col4': 12},
                   's4': {'col1': 13, 'col2': 14, 'col3': 15, 'col4': 16}}},
 'level2': {'t1': {'s1': {'col1': 5, 'col2': 4, 'col3': 9, 'col4': 9},
                   's2': {'col1': 1, 'col2': 5, 'col3': 4, 'col4': 5},
                   's3': {'col1': 11, 'col2': 8, 'col3': 2, 'col4': 13},
                   's4': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 20}},
            't2': {'s1': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9},
                   's2': {'col1': 1, 'col2': 5, 'col3': 4, 'col4': 8},
                   's3': {'col1': 11, 'col2': 8, 'col3': 2, 'col4': 9},
                   's4': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9}},
            't3': {'s1': {'col1': 1, 'col2': 2, 'col3': 3, 'col4': 4},
                   's2': {'col1': 5, 'col2': 6, 'col3': 7, 'col4': 8},
                   's3': {'col1': 9, 'col2': 10, 'col3': 11, 'col4': 12},
                   's4': {'col1': 13, 'col2': 14, 'col3': 15, 'col4': 16}}}}
pprint(list(fla_tu(data)))

print('------------------------------------------')
#with protection
data={'level1': {'t1': {'s1': ProtectedDict({'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9}),
                   's2': {'col1': 1, 'col2': 5, 'col3': 4, 'col4': 8},
                   's3': {'col1': 11, 'col2': 8, 'col3': 2, 'col4': 9},
                   's4': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9}},
            't2': {'s1': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9},
                   's2': {'col1': 1, 'col2': 5, 'col3': 4, 'col4': 8},
                   's3': {'col1': 11, 'col2': 8, 'col3': 2, 'col4': 9},
                   's4': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9}},
            't3': ProtectedDict({'s1': {'col1': 1, 'col2': 2, 'col3': 3, 'col4': 4},
                   's2': {'col1': 5, 'col2': 6, 'col3': 7, 'col4': 8},
                   's3': {'col1': 9, 'col2': 10, 'col3': 11, 'col4': 12},
                   's4': {'col1': 13, 'col2': 14, 'col3': 15, 'col4': 16}})},
 'level2': {'t1': {'s1': {'col1': 5, 'col2': 4, 'col3': 9, 'col4': 9},
                   's2': {'col1': 1, 'col2': 5, 'col3': 4, 'col4': 5},
                   's3': {'col1': 11, 'col2': ProtectedList([8,3,5,23,'342342']), 'col3': 2, 'col4': 13},
                   's4': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 20}},
            't2': {'s1': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9},
                   's2': {'col1': 1, 'col2': 5, 'col3': 4, 'col4': 8},
                   's3': {'col1': 11, 'col2': 8, 'col3': 2, 'col4': 9},
                   's4': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9}},
            't3': {'s1': {'col1': 1, 'col2': (2,3,4,5), 'col3': ProtectedTuple((2,3,4,5,'32123')), 'col4': 4},
                   's2': {'col1': 5, 'col2': 6, 'col3': 7, 'col4': 8},
                   's3': {'col1': 9, 'col2': 10, 'col3': 11, 'col4': 12},
                   's4': {'col1': 13, 'col2': 14, 'col3': 15, 'col4': 16}}}}
pprint(list(list(fla_tu(data)))) #Without protection
[(5, ('level1', 't1', 's1', 'col1')),
 (4, ('level1', 't1', 's1', 'col2')),
 (4, ('level1', 't1', 's1', 'col3')),
 (9, ('level1', 't1', 's1', 'col4')),
 (1, ('level1', 't1', 's2', 'col1')),
 (5, ('level1', 't1', 's2', 'col2')),
 (4, ('level1', 't1', 's2', 'col3')),
 (8, ('level1', 't1', 's2', 'col4')),
 (11, ('level1', 't1', 's3', 'col1')),
 (8, ('level1', 't1', 's3', 'col2')),
 (2, ('level1', 't1', 's3', 'col3')),
 (9, ('level1', 't1', 's3', 'col4')),
 (5, ('level1', 't1', 's4', 'col1')),
 (4, ('level1', 't1', 's4', 'col2')),
 (4, ('level1', 't1', 's4', 'col3')),
 (9, ('level1', 't1', 's4', 'col4')),
 (5, ('level1', 't2', 's1', 'col1')),
 (4, ('level1', 't2', 's1', 'col2')),
 (4, ('level1', 't2', 's1', 'col3')),
 (9, ('level1', 't2', 's1', 'col4')),
 (1, ('level1', 't2', 's2', 'col1')),
 (5, ('level1', 't2', 's2', 'col2')),
 (4, ('level1', 't2', 's2', 'col3')),
 (8, ('level1', 't2', 's2', 'col4')),
 (11, ('level1', 't2', 's3', 'col1')),
 (8, ('level1', 't2', 's3', 'col2')),
 (2, ('level1', 't2', 's3', 'col3')),
 (9, ('level1', 't2', 's3', 'col4')),
 (5, ('level1', 't2', 's4', 'col1')),
 (4, ('level1', 't2', 's4', 'col2')),
 (4, ('level1', 't2', 's4', 'col3')),
 (9, ('level1', 't2', 's4', 'col4')),
 (1, ('level1', 't3', 's1', 'col1')),
 (2, ('level1', 't3', 's1', 'col2')),
 (3, ('level1', 't3', 's1', 'col3')),
 (4, ('level1', 't3', 's1', 'col4')),
 (5, ('level1', 't3', 's2', 'col1')),
 (6, ('level1', 't3', 's2', 'col2')),
 (7, ('level1', 't3', 's2', 'col3')),
 (8, ('level1', 't3', 's2', 'col4')),
 (9, ('level1', 't3', 's3', 'col1')),
 (10, ('level1', 't3', 's3', 'col2')),
 (11, ('level1', 't3', 's3', 'col3')),
 (12, ('level1', 't3', 's3', 'col4')),
 (13, ('level1', 't3', 's4', 'col1')),
 (14, ('level1', 't3', 's4', 'col2')),
 (15, ('level1', 't3', 's4', 'col3')),
 (16, ('level1', 't3', 's4', 'col4')),
 (5, ('level2', 't1', 's1', 'col1')),
 (4, ('level2', 't1', 's1', 'col2')),
 (9, ('level2', 't1', 's1', 'col3')),
 (9, ('level2', 't1', 's1', 'col4')),
 (1, ('level2', 't1', 's2', 'col1')),
 (5, ('level2', 't1', 's2', 'col2')),
 (4, ('level2', 't1', 's2', 'col3')),
 (5, ('level2', 't1', 's2', 'col4')),
 (11, ('level2', 't1', 's3', 'col1')),
 (8, ('level2', 't1', 's3', 'col2')),
 (2, ('level2', 't1', 's3', 'col3')),
 (13, ('level2', 't1', 's3', 'col4')),
 (5, ('level2', 't1', 's4', 'col1')),
 (4, ('level2', 't1', 's4', 'col2')),
 (4, ('level2', 't1', 's4', 'col3')),
 (20, ('level2', 't1', 's4', 'col4')),
 (5, ('level2', 't2', 's1', 'col1')),
 (4, ('level2', 't2', 's1', 'col2')),
 (4, ('level2', 't2', 's1', 'col3')),
 (9, ('level2', 't2', 's1', 'col4')),
 (1, ('level2', 't2', 's2', 'col1')),
 (5, ('level2', 't2', 's2', 'col2')),
 (4, ('level2', 't2', 's2', 'col3')),
 (8, ('level2', 't2', 's2', 'col4')),
 (11, ('level2', 't2', 's3', 'col1')),
 (8, ('level2', 't2', 's3', 'col2')),
 (2, ('level2', 't2', 's3', 'col3')),
 (9, ('level2', 't2', 's3', 'col4')),
 (5, ('level2', 't2', 's4', 'col1')),
 (4, ('level2', 't2', 's4', 'col2')),
 (4, ('level2', 't2', 's4', 'col3')),
 (9, ('level2', 't2', 's4', 'col4')),
 (1, ('level2', 't3', 's1', 'col1')),
 (2, ('level2', 't3', 's1', 'col2')),
 (3, ('level2', 't3', 's1', 'col3')),
 (4, ('level2', 't3', 's1', 'col4')),
 (5, ('level2', 't3', 's2', 'col1')),
 (6, ('level2', 't3', 's2', 'col2')),
 (7, ('level2', 't3', 's2', 'col3')),
 (8, ('level2', 't3', 's2', 'col4')),
 (9, ('level2', 't3', 's3', 'col1')),
 (10, ('level2', 't3', 's3', 'col2')),
 (11, ('level2', 't3', 's3', 'col3')),
 (12, ('level2', 't3', 's3', 'col4')),
 (13, ('level2', 't3', 's4', 'col1')),
 (14, ('level2', 't3', 's4', 'col2')),
 (15, ('level2', 't3', 's4', 'col3')),
 (16, ('level2', 't3', 's4', 'col4'))]
------------------------------------------ #With protection
[({'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9}, ('level1', 't1', 's1')),
 (1, ('level1', 't1', 's2', 'col1')),
 (5, ('level1', 't1', 's2', 'col2')),
 (4, ('level1', 't1', 's2', 'col3')),
 (8, ('level1', 't1', 's2', 'col4')),
 (11, ('level1', 't1', 's3', 'col1')),
 (8, ('level1', 't1', 's3', 'col2')),
 (2, ('level1', 't1', 's3', 'col3')),
 (9, ('level1', 't1', 's3', 'col4')),
 (5, ('level1', 't1', 's4', 'col1')),
 (4, ('level1', 't1', 's4', 'col2')),
 (4, ('level1', 't1', 's4', 'col3')),
 (9, ('level1', 't1', 's4', 'col4')),
 (5, ('level1', 't2', 's1', 'col1')),
 (4, ('level1', 't2', 's1', 'col2')),
 (4, ('level1', 't2', 's1', 'col3')),
 (9, ('level1', 't2', 's1', 'col4')),
 (1, ('level1', 't2', 's2', 'col1')),
 (5, ('level1', 't2', 's2', 'col2')),
 (4, ('level1', 't2', 's2', 'col3')),
 (8, ('level1', 't2', 's2', 'col4')),
 (11, ('level1', 't2', 's3', 'col1')),
 (8, ('level1', 't2', 's3', 'col2')),
 (2, ('level1', 't2', 's3', 'col3')),
 (9, ('level1', 't2', 's3', 'col4')),
 (5, ('level1', 't2', 's4', 'col1')),
 (4, ('level1', 't2', 's4', 'col2')),
 (4, ('level1', 't2', 's4', 'col3')),
 (9, ('level1', 't2', 's4', 'col4')),
 ({'s1': {'col1': 1, 'col2': 2, 'col3': 3, 'col4': 4},
   's2': {'col1': 5, 'col2': 6, 'col3': 7, 'col4': 8},
   's3': {'col1': 9, 'col2': 10, 'col3': 11, 'col4': 12},
   's4': {'col1': 13, 'col2': 14, 'col3': 15, 'col4': 16}},
  ('level1', 't3')),
 (5, ('level2', 't1', 's1', 'col1')),
 (4, ('level2', 't1', 's1', 'col2')),
 (9, ('level2', 't1', 's1', 'col3')),
 (9, ('level2', 't1', 's1', 'col4')),
 (1, ('level2', 't1', 's2', 'col1')),
 (5, ('level2', 't1', 's2', 'col2')),
 (4, ('level2', 't1', 's2', 'col3')),
 (5, ('level2', 't1', 's2', 'col4')),
 (11, ('level2', 't1', 's3', 'col1')),
 ([8, 3, 5, 23, '342342'], ('level2', 't1', 's3', 'col2')),
 (2, ('level2', 't1', 's3', 'col3')),
 (13, ('level2', 't1', 's3', 'col4')),
 (5, ('level2', 't1', 's4', 'col1')),
 (4, ('level2', 't1', 's4', 'col2')),
 (4, ('level2', 't1', 's4', 'col3')),
 (20, ('level2', 't1', 's4', 'col4')),
 (5, ('level2', 't2', 's1', 'col1')),
 (4, ('level2', 't2', 's1', 'col2')),
 (4, ('level2', 't2', 's1', 'col3')),
 (9, ('level2', 't2', 's1', 'col4')),
 (1, ('level2', 't2', 's2', 'col1')),
 (5, ('level2', 't2', 's2', 'col2')),
 (4, ('level2', 't2', 's2', 'col3')),
 (8, ('level2', 't2', 's2', 'col4')),
 (11, ('level2', 't2', 's3', 'col1')),
 (8, ('level2', 't2', 's3', 'col2')),
 (2, ('level2', 't2', 's3', 'col3')),
 (9, ('level2', 't2', 's3', 'col4')),
 (5, ('level2', 't2', 's4', 'col1')),
 (4, ('level2', 't2', 's4', 'col2')),
 (4, ('level2', 't2', 's4', 'col3')),
 (9, ('level2', 't2', 's4', 'col4')),
 (1, ('level2', 't3', 's1', 'col1')),
 (2, ('level2', 't3', 's1', 'col2', 0)),
 (3, ('level2', 't3', 's1', 'col2', 1)),
 (4, ('level2', 't3', 's1', 'col2', 2)),
 (5, ('level2', 't3', 's1', 'col2', 3)),
 ((2, 3, 4, 5, '32123'), ('level2', 't3', 's1', 'col3')),
 (4, ('level2', 't3', 's1', 'col4')),
 (5, ('level2', 't3', 's2', 'col1')),
 (6, ('level2', 't3', 's2', 'col2')),
 (7, ('level2', 't3', 's2', 'col3')),
 (8, ('level2', 't3', 's2', 'col4')),
 (9, ('level2', 't3', 's3', 'col1')),
 (10, ('level2', 't3', 's3', 'col2')),
 (11, ('level2', 't3', 's3', 'col3')),
 (12, ('level2', 't3', 's3', 'col4')),
 (13, ('level2', 't3', 's4', 'col1')),
 (14, ('level2', 't3', 's4', 'col2')),
 (15, ('level2', 't3', 's4', 'col3')),
 (16, ('level2', 't3', 's4', 'col4'))]
```

### Install

```python
pip install flatten-any-dict-iterable-or-whatsoever
```

### Usage

```python
from flatten_any_dict_iterable_or_whatsoever import flatten_nested_something_to_list_of_tuples
flatten_nested_something_to_list_of_tuples(nested_iter_that_drives_me_crazy) #That's it! :)
```

### Examples

```python
https://stackoverflow.com/questions/72990265/convert-nested-list-in-dictionary-to-dataframe/72990346
before:
{'a': 'test',
 'b': 1657,
 'c': 'asset',
 'd': [['2089', '0.0'], ['2088', '0.0']],
 'e': [['2088', '0.0'], ['2088', '0.0'], ['2088', '0.00']],
 'f': [['2088', '0.0', 'x', 'foo'],
       ['2088', '0.0', 'bar', 'i'],
       ['2088', '0.00', 'z', '0.2']],
 'x': ['test1', 'test2']}
Let's flatten it: flatten_nested_something_to_list_of_tuples(data)
value: test                                     keys: ('a',)
value: 1657                                     keys: ('b',)
value: asset                                    keys: ('c',)
value: 2089                                     keys: ('d', 0)
value: 0.0                                      keys: ('d', 0)
value: 2088                                     keys: ('d', 1)
value: 0.0                                      keys: ('d', 1)
value: 2088                                     keys: ('e', 0)
value: 0.0                                      keys: ('e', 0)
value: 2088                                     keys: ('e', 1)
value: 0.0                                      keys: ('e', 1)
value: 2088                                     keys: ('e', 2)
value: 0.00                                     keys: ('e', 2)
value: 2088                                     keys: ('f', 0)
value: 0.0                                      keys: ('f', 0)
value: x                                        keys: ('f', 0)
value: foo                                      keys: ('f', 0)
value: 2088                                     keys: ('f', 1)
value: 0.0                                      keys: ('f', 1)
value: bar                                      keys: ('f', 1)
value: i                                        keys: ('f', 1)
value: 2088                                     keys: ('f', 2)
value: 0.00                                     keys: ('f', 2)
value: z                                        keys: ('f', 2)
value: 0.2                                      keys: ('f', 2)
value: test1                                    keys: ('x',)
value: test2                                    keys: ('x',)
https://stackoverflow.com/questions/73430585/how-to-convert-a-list-of-nested-dictionaries-includes-tuples-as-a-dataframe
before:
[{'cb': ({'ID': 1, 'Name': 'A', 'num': 50}, {'ID': 2, 'Name': 'A', 'num': 68}),
  'final_value': 118},
 {'cb': ({'ID': 1, 'Name': 'A', 'num': 50}, {'ID': 4, 'Name': 'A', 'num': 67}),
  'final_value': 117},
 {'cb': ({'ID': 1, 'Name': 'A', 'num': 50}, {'ID': 6, 'Name': 'A', 'num': 67}),
  'final_value': 117}]
Let's flatten it: flatten_nested_something_to_list_of_tuples(data)
value: A                                        keys: (0, 'cb', 0, 'Name')
value: 1                                        keys: (0, 'cb', 0, 'ID')
value: 50                                       keys: (0, 'cb', 0, 'num')
value: A                                        keys: (0, 'cb', 1, 'Name')
value: 2                                        keys: (0, 'cb', 1, 'ID')
value: 68                                       keys: (0, 'cb', 1, 'num')
value: 118                                      keys: (0, 'final_value')
value: A                                        keys: (1, 'cb', 0, 'Name')
value: 1                                        keys: (1, 'cb', 0, 'ID')
value: 50                                       keys: (1, 'cb', 0, 'num')
value: A                                        keys: (1, 'cb', 1, 'Name')
value: 4                                        keys: (1, 'cb', 1, 'ID')
value: 67                                       keys: (1, 'cb', 1, 'num')
value: 117                                      keys: (1, 'final_value')
value: A                                        keys: (2, 'cb', 0, 'Name')
value: 1                                        keys: (2, 'cb', 0, 'ID')
value: 50                                       keys: (2, 'cb', 0, 'num')
value: A                                        keys: (2, 'cb', 1, 'Name')
value: 6                                        keys: (2, 'cb', 1, 'ID')
value: 67                                       keys: (2, 'cb', 1, 'num')
value: 117                                      keys: (2, 'final_value')
https://stackoverflow.com/questions/69943509/problems-when-flatten-a-dict
before:
[{'application_contacts': [{'adress': 'X', 'email': 'test@test.com'}],
  'application_details': {'email': None, 'phone': None},
  'employer': {'Name': 'Nom', 'email': None},
  'id': '1'},
 {'application_contacts': [{'adress': 'Z', 'email': None}],
  'application_details': {'email': 'testy@test_a.com', 'phone': None},
  'employer': {'Name': 'Nom', 'email': None},
  'id': '2'},
 {'application_contacts': [{'adress': 'Y', 'email': None}],
  'application_details': {'email': 'testy@test_a.com', 'phone': None},
  'employer': {'Name': 'Nom', 'email': None},
  'id': '3'}]
Let's flatten it: flatten_nested_something_to_list_of_tuples(data)
value: 1                                        keys: (0, 'id')
value: None                                     keys: (0, 'application_details', 'phone')
value: None                                     keys: (0, 'application_details', 'email')
value: Nom                                      keys: (0, 'employer', 'Name')
value: None                                     keys: (0, 'employer', 'email')
value: test@test.com                            keys: (0, 'application_contacts', 0, 'email')
value: X                                        keys: (0, 'application_contacts', 0, 'adress')
value: 2                                        keys: (1, 'id')
value: None                                     keys: (1, 'application_details', 'phone')
value: testy@test_a.com                         keys: (1, 'application_details', 'email')
value: Nom                                      keys: (1, 'employer', 'Name')
value: None                                     keys: (1, 'employer', 'email')
value: None                                     keys: (1, 'application_contacts', 0, 'email')
value: Z                                        keys: (1, 'application_contacts', 0, 'adress')
value: 3                                        keys: (2, 'id')
value: None                                     keys: (2, 'application_details', 'phone')
value: testy@test_a.com                         keys: (2, 'application_details', 'email')
value: Nom                                      keys: (2, 'employer', 'Name')
value: None                                     keys: (2, 'employer', 'email')
value: None                                     keys: (2, 'application_contacts', 0, 'email')
value: Y                                        keys: (2, 'application_contacts', 0, 'adress')
https://stackoverflow.com/questions/62765371/convert-nested-dataframe-to-a-simple-dataframeframe
before:
{'A': [1, 2, 3],
 'B': [4, 5, 6],
 'departure': [{'actual': None,
                'actual_runway': None,
                'airport': 'Findel',
                'delay': None,
                'estimated': '2020-07-07T06:30:00+00:00',
                'estimated_runway': None,
                'gate': None,
                'iata': 'LUX',
                'icao': 'ELLX',
                'scheduled': '2020-07-07T06:30:00+00:00',
                'terminal': None,
                'timezone': 'Europe/Luxembourg'},
               {'actual': None,
                'actual_runway': None,
                'airport': 'Findel',
                'delay': None,
                'estimated': '2020-07-07T06:30:00+00:00',
                'estimated_runway': None,
                'gate': None,
                'iata': 'LUX',
                'icao': 'ELLX',
                'scheduled': '2020-07-07T06:30:00+00:00',
                'terminal': None,
                'timezone': 'Europe/Luxembourg'},
               {'actual': None,
                'actual_runway': None,
                'airport': 'Findel',
                'delay': None,
                'estimated': '2020-07-07T06:30:00+00:00',
                'estimated_runway': None,
                'gate': None,
                'iata': 'LUX',
                'icao': 'ELLX',
                'scheduled': '2020-07-07T06:30:00+00:00',
                'terminal': None,
                'timezone': 'Europe/Luxembourg'}]}
Let's flatten it: flatten_nested_something_to_list_of_tuples(data)
value: 1                                        keys: ('A',)
value: 2                                        keys: ('A',)
value: 3                                        keys: ('A',)
value: 4                                        keys: ('B',)
value: 5                                        keys: ('B',)
value: 6                                        keys: ('B',)
value: Findel                                   keys: ('departure', 0, 'airport')
value: Europe/Luxembourg                        keys: ('departure', 0, 'timezone')
value: LUX                                      keys: ('departure', 0, 'iata')
value: ELLX                                     keys: ('departure', 0, 'icao')
value: None                                     keys: ('departure', 0, 'terminal')
value: None                                     keys: ('departure', 0, 'gate')
value: None                                     keys: ('departure', 0, 'delay')
value: 2020-07-07T06:30:00+00:00                keys: ('departure', 0, 'scheduled')
value: 2020-07-07T06:30:00+00:00                keys: ('departure', 0, 'estimated')
value: None                                     keys: ('departure', 0, 'actual')
value: None                                     keys: ('departure', 0, 'estimated_runway')
value: None                                     keys: ('departure', 0, 'actual_runway')
value: Findel                                   keys: ('departure', 1, 'airport')
value: Europe/Luxembourg                        keys: ('departure', 1, 'timezone')
value: LUX                                      keys: ('departure', 1, 'iata')
value: ELLX                                     keys: ('departure', 1, 'icao')
value: None                                     keys: ('departure', 1, 'terminal')
value: None                                     keys: ('departure', 1, 'gate')
value: None                                     keys: ('departure', 1, 'delay')
value: 2020-07-07T06:30:00+00:00                keys: ('departure', 1, 'scheduled')
value: 2020-07-07T06:30:00+00:00                keys: ('departure', 1, 'estimated')
value: None                                     keys: ('departure', 1, 'actual')
value: None                                     keys: ('departure', 1, 'estimated_runway')
value: None                                     keys: ('departure', 1, 'actual_runway')
value: Findel                                   keys: ('departure', 2, 'airport')
value: Europe/Luxembourg                        keys: ('departure', 2, 'timezone')
value: LUX                                      keys: ('departure', 2, 'iata')
value: ELLX                                     keys: ('departure', 2, 'icao')
value: None                                     keys: ('departure', 2, 'terminal')
value: None                                     keys: ('departure', 2, 'gate')
value: None                                     keys: ('departure', 2, 'delay')
value: 2020-07-07T06:30:00+00:00                keys: ('departure', 2, 'scheduled')
value: 2020-07-07T06:30:00+00:00                keys: ('departure', 2, 'estimated')
value: None                                     keys: ('departure', 2, 'actual')
value: None                                     keys: ('departure', 2, 'estimated_runway')
value: None                                     keys: ('departure', 2, 'actual_runway')
https://stackoverflow.com/questions/64359762/constructing-a-pandas-dataframe-with-columns-and-sub-columns-from-nested-diction
before:
{'level1': {'t1': {'s1': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9},
                   's2': {'col1': 1, 'col2': 5, 'col3': 4, 'col4': 8},
                   's3': {'col1': 11, 'col2': 8, 'col3': 2, 'col4': 9},
                   's4': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9}},
            't2': {'s1': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9},
                   's2': {'col1': 1, 'col2': 5, 'col3': 4, 'col4': 8},
                   's3': {'col1': 11, 'col2': 8, 'col3': 2, 'col4': 9},
                   's4': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9}},
            't3': {'s1': {'col1': 1, 'col2': 2, 'col3': 3, 'col4': 4},
                   's2': {'col1': 5, 'col2': 6, 'col3': 7, 'col4': 8},
                   's3': {'col1': 9, 'col2': 10, 'col3': 11, 'col4': 12},
                   's4': {'col1': 13, 'col2': 14, 'col3': 15, 'col4': 16}}},
 'level2': {'t1': {'s1': {'col1': 5, 'col2': 4, 'col3': 9, 'col4': 9},
                   's2': {'col1': 1, 'col2': 5, 'col3': 4, 'col4': 5},
                   's3': {'col1': 11, 'col2': 8, 'col3': 2, 'col4': 13},
                   's4': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 20}},
            't2': {'s1': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9},
                   's2': {'col1': 1, 'col2': 5, 'col3': 4, 'col4': 8},
                   's3': {'col1': 11, 'col2': 8, 'col3': 2, 'col4': 9},
                   's4': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9}},
            't3': {'s1': {'col1': 1, 'col2': 2, 'col3': 3, 'col4': 4},
                   's2': {'col1': 5, 'col2': 6, 'col3': 7, 'col4': 8},
                   's3': {'col1': 9, 'col2': 10, 'col3': 11, 'col4': 12},
                   's4': {'col1': 13, 'col2': 14, 'col3': 15, 'col4': 16}}}}
Let's flatten it: flatten_nested_something_to_list_of_tuples(data)
value: 5                                        keys: ('level1', 't1', 's1', 'col1')
value: 4                                        keys: ('level1', 't1', 's1', 'col2')
value: 4                                        keys: ('level1', 't1', 's1', 'col3')
value: 9                                        keys: ('level1', 't1', 's1', 'col4')
value: 1                                        keys: ('level1', 't1', 's2', 'col1')
value: 5                                        keys: ('level1', 't1', 's2', 'col2')
value: 4                                        keys: ('level1', 't1', 's2', 'col3')
value: 8                                        keys: ('level1', 't1', 's2', 'col4')
value: 11                                       keys: ('level1', 't1', 's3', 'col1')
value: 8                                        keys: ('level1', 't1', 's3', 'col2')
value: 2                                        keys: ('level1', 't1', 's3', 'col3')
value: 9                                        keys: ('level1', 't1', 's3', 'col4')
value: 5                                        keys: ('level1', 't1', 's4', 'col1')
value: 4                                        keys: ('level1', 't1', 's4', 'col2')
value: 4                                        keys: ('level1', 't1', 's4', 'col3')
value: 9                                        keys: ('level1', 't1', 's4', 'col4')
value: 5                                        keys: ('level1', 't2', 's1', 'col1')
value: 4                                        keys: ('level1', 't2', 's1', 'col2')
value: 4                                        keys: ('level1', 't2', 's1', 'col3')
value: 9                                        keys: ('level1', 't2', 's1', 'col4')
value: 1                                        keys: ('level1', 't2', 's2', 'col1')
value: 5                                        keys: ('level1', 't2', 's2', 'col2')
value: 4                                        keys: ('level1', 't2', 's2', 'col3')
value: 8                                        keys: ('level1', 't2', 's2', 'col4')
value: 11                                       keys: ('level1', 't2', 's3', 'col1')
value: 8                                        keys: ('level1', 't2', 's3', 'col2')
value: 2                                        keys: ('level1', 't2', 's3', 'col3')
value: 9                                        keys: ('level1', 't2', 's3', 'col4')
value: 5                                        keys: ('level1', 't2', 's4', 'col1')
value: 4                                        keys: ('level1', 't2', 's4', 'col2')
value: 4                                        keys: ('level1', 't2', 's4', 'col3')
value: 9                                        keys: ('level1', 't2', 's4', 'col4')
value: 1                                        keys: ('level1', 't3', 's1', 'col1')
value: 2                                        keys: ('level1', 't3', 's1', 'col2')
value: 3                                        keys: ('level1', 't3', 's1', 'col3')
value: 4                                        keys: ('level1', 't3', 's1', 'col4')
value: 5                                        keys: ('level1', 't3', 's2', 'col1')
value: 6                                        keys: ('level1', 't3', 's2', 'col2')
value: 7                                        keys: ('level1', 't3', 's2', 'col3')
value: 8                                        keys: ('level1', 't3', 's2', 'col4')
value: 9                                        keys: ('level1', 't3', 's3', 'col1')
value: 10                                       keys: ('level1', 't3', 's3', 'col2')
value: 11                                       keys: ('level1', 't3', 's3', 'col3')
value: 12                                       keys: ('level1', 't3', 's3', 'col4')
value: 13                                       keys: ('level1', 't3', 's4', 'col1')
value: 14                                       keys: ('level1', 't3', 's4', 'col2')
value: 15                                       keys: ('level1', 't3', 's4', 'col3')
value: 16                                       keys: ('level1', 't3', 's4', 'col4')
value: 5                                        keys: ('level2', 't1', 's1', 'col1')
value: 4                                        keys: ('level2', 't1', 's1', 'col2')
value: 9                                        keys: ('level2', 't1', 's1', 'col3')
value: 9                                        keys: ('level2', 't1', 's1', 'col4')
value: 1                                        keys: ('level2', 't1', 's2', 'col1')
value: 5                                        keys: ('level2', 't1', 's2', 'col2')
value: 4                                        keys: ('level2', 't1', 's2', 'col3')
value: 5                                        keys: ('level2', 't1', 's2', 'col4')
value: 11                                       keys: ('level2', 't1', 's3', 'col1')
value: 8                                        keys: ('level2', 't1', 's3', 'col2')
value: 2                                        keys: ('level2', 't1', 's3', 'col3')
value: 13                                       keys: ('level2', 't1', 's3', 'col4')
value: 5                                        keys: ('level2', 't1', 's4', 'col1')
value: 4                                        keys: ('level2', 't1', 's4', 'col2')
value: 4                                        keys: ('level2', 't1', 's4', 'col3')
value: 20                                       keys: ('level2', 't1', 's4', 'col4')
value: 5                                        keys: ('level2', 't2', 's1', 'col1')
value: 4                                        keys: ('level2', 't2', 's1', 'col2')
value: 4                                        keys: ('level2', 't2', 's1', 'col3')
value: 9                                        keys: ('level2', 't2', 's1', 'col4')
value: 1                                        keys: ('level2', 't2', 's2', 'col1')
value: 5                                        keys: ('level2', 't2', 's2', 'col2')
value: 4                                        keys: ('level2', 't2', 's2', 'col3')
value: 8                                        keys: ('level2', 't2', 's2', 'col4')
value: 11                                       keys: ('level2', 't2', 's3', 'col1')
value: 8                                        keys: ('level2', 't2', 's3', 'col2')
value: 2                                        keys: ('level2', 't2', 's3', 'col3')
value: 9                                        keys: ('level2', 't2', 's3', 'col4')
value: 5                                        keys: ('level2', 't2', 's4', 'col1')
value: 4                                        keys: ('level2', 't2', 's4', 'col2')
value: 4                                        keys: ('level2', 't2', 's4', 'col3')
value: 9                                        keys: ('level2', 't2', 's4', 'col4')
value: 1                                        keys: ('level2', 't3', 's1', 'col1')
value: 2                                        keys: ('level2', 't3', 's1', 'col2')
value: 3                                        keys: ('level2', 't3', 's1', 'col3')
value: 4                                        keys: ('level2', 't3', 's1', 'col4')
value: 5                                        keys: ('level2', 't3', 's2', 'col1')
value: 6                                        keys: ('level2', 't3', 's2', 'col2')
value: 7                                        keys: ('level2', 't3', 's2', 'col3')
value: 8                                        keys: ('level2', 't3', 's2', 'col4')
value: 9                                        keys: ('level2', 't3', 's3', 'col1')
value: 10                                       keys: ('level2', 't3', 's3', 'col2')
value: 11                                       keys: ('level2', 't3', 's3', 'col3')
value: 12                                       keys: ('level2', 't3', 's3', 'col4')
value: 13                                       keys: ('level2', 't3', 's4', 'col1')
value: 14                                       keys: ('level2', 't3', 's4', 'col2')
value: 15                                       keys: ('level2', 't3', 's4', 'col3')
value: 16                                       keys: ('level2', 't3', 's4', 'col4')
https://stackoverflow.com/questions/61984148/how-to-handle-nested-lists-and-dictionaries-in-pandas-dataframe
before:
{'critic_reviews': [{'review_critic': 'XYZ', 'review_score': 90},
                    {'review_critic': 'ABC', 'review_score': 90},
                    {'review_critic': '123', 'review_score': 90}],
 'genres': ['Sports', 'Golf'],
 'score': 85,
 'title': 'Golf Simulator',
 'url': 'http://example.com/golf-simulator'}
Let's flatten it: flatten_nested_something_to_list_of_tuples(data)
value: Golf Simulator                           keys: ('title',)
value: Sports                                   keys: ('genres',)
value: Golf                                     keys: ('genres',)
value: 85                                       keys: ('score',)
value: XYZ                                      keys: ('critic_reviews', 0, 'review_critic')
value: 90                                       keys: ('critic_reviews', 0, 'review_score')
value: ABC                                      keys: ('critic_reviews', 1, 'review_critic')
value: 90                                       keys: ('critic_reviews', 1, 'review_score')
value: 123                                      keys: ('critic_reviews', 2, 'review_critic')
value: 90                                       keys: ('critic_reviews', 2, 'review_score')
value: http://example.com/golf-simulator        keys: ('url',)
https://stackoverflow.com/questions/72146094/problems-matching-values-from-nested-dictionary
before:
{'_links': {'next': None, 'prev': None},
 'limit': 250,
 'offset': 0,
 'runs': [{'assignedto_id': None,
           'blocked_count': 0,
           'completed_on': None,
           'config': None,
           'config_ids': [],
           'created_by': 1,
           'created_on': 1651790693,
           'custom_status1_count': 0,
           'custom_status2_count': 0,
           'custom_status3_count': 0,
           'custom_status4_count': 0,
           'custom_status5_count': 0,
           'custom_status6_count': 0,
           'custom_status7_count': 0,
           'description': None,
           'failed_count': 1,
           'id': 13,
           'include_all': False,
           'is_completed': False,
           'milestone_id': None,
           'name': '2022-05-05-testrun',
           'passed_count': 2,
           'plan_id': None,
           'project_id': 1,
           'refs': None,
           'retest_count': 0,
           'suite_id': 1,
           'untested_count': 0,
           'updated_on': 1651790693,
           'url': 'https://xxxxxxxxxx.testrail.io/index.php?/runs/view/13'},
          {'assignedto_id': None,
           'blocked_count': 0,
           'completed_on': 1650989972,
           'config': None,
           'config_ids': [],
           'created_by': 5,
           'created_on': 1650966329,
           'custom_status1_count': 0,
           'custom_status2_count': 0,
           'custom_status3_count': 0,
           'custom_status4_count': 0,
           'custom_status5_count': 0,
           'custom_status6_count': 0,
           'custom_status7_count': 0,
           'description': None,
           'failed_count': 0,
           'id': 9,
           'include_all': False,
           'is_completed': True,
           'milestone_id': None,
           'name': 'This is a new test run',
           'passed_count': 0,
           'plan_id': None,
           'project_id': 1,
           'refs': None,
           'retest_count': 0,
           'suite_id': 1,
           'untested_count': 3,
           'updated_on': 1650966329,
           'url': 'https://xxxxxxxxxx.testrail.io/index.php?/runs/view/9'}],
 'size': 2}
Let's flatten it: flatten_nested_something_to_list_of_tuples(data)
value: None                                     keys: ('_links', 'next')
value: None                                     keys: ('_links', 'prev')
value: 250                                      keys: ('limit',)
value: 0                                        keys: ('offset',)
value: None                                     keys: ('runs', 0, 'assignedto_id')
value: 0                                        keys: ('runs', 0, 'blocked_count')
value: None                                     keys: ('runs', 0, 'completed_on')
value: None                                     keys: ('runs', 0, 'config')
value: 1                                        keys: ('runs', 0, 'created_by')
value: 1651790693                               keys: ('runs', 0, 'created_on')
value: 0                                        keys: ('runs', 0, 'custom_status1_count')
value: 0                                        keys: ('runs', 0, 'custom_status2_count')
value: 0                                        keys: ('runs', 0, 'custom_status3_count')
value: 0                                        keys: ('runs', 0, 'custom_status4_count')
value: 0                                        keys: ('runs', 0, 'custom_status5_count')
value: 0                                        keys: ('runs', 0, 'custom_status6_count')
value: 0                                        keys: ('runs', 0, 'custom_status7_count')
value: None                                     keys: ('runs', 0, 'description')
value: 1                                        keys: ('runs', 0, 'failed_count')
value: 13                                       keys: ('runs', 0, 'id')
value: False                                    keys: ('runs', 0, 'include_all')
value: False                                    keys: ('runs', 0, 'is_completed')
value: None                                     keys: ('runs', 0, 'milestone_id')
value: 2022-05-05-testrun                       keys: ('runs', 0, 'name')
value: 2                                        keys: ('runs', 0, 'passed_count')
value: None                                     keys: ('runs', 0, 'plan_id')
value: 1                                        keys: ('runs', 0, 'project_id')
value: None                                     keys: ('runs', 0, 'refs')
value: 0                                        keys: ('runs', 0, 'retest_count')
value: 1                                        keys: ('runs', 0, 'suite_id')
value: 0                                        keys: ('runs', 0, 'untested_count')
value: 1651790693                               keys: ('runs', 0, 'updated_on')
value: https://xxxxxxxxxx.testrail.io/index.php?/runs/view/13 keys: ('runs', 0, 'url')
value: None                                     keys: ('runs', 1, 'assignedto_id')
value: 0                                        keys: ('runs', 1, 'blocked_count')
value: 1650989972                               keys: ('runs', 1, 'completed_on')
value: None                                     keys: ('runs', 1, 'config')
value: 5                                        keys: ('runs', 1, 'created_by')
value: 1650966329                               keys: ('runs', 1, 'created_on')
value: 0                                        keys: ('runs', 1, 'custom_status1_count')
value: 0                                        keys: ('runs', 1, 'custom_status2_count')
value: 0                                        keys: ('runs', 1, 'custom_status3_count')
value: 0                                        keys: ('runs', 1, 'custom_status4_count')
value: 0                                        keys: ('runs', 1, 'custom_status5_count')
value: 0                                        keys: ('runs', 1, 'custom_status6_count')
value: 0                                        keys: ('runs', 1, 'custom_status7_count')
value: None                                     keys: ('runs', 1, 'description')
value: 0                                        keys: ('runs', 1, 'failed_count')
value: 9                                        keys: ('runs', 1, 'id')
value: False                                    keys: ('runs', 1, 'include_all')
value: True                                     keys: ('runs', 1, 'is_completed')
value: None                                     keys: ('runs', 1, 'milestone_id')
value: This is a new test run                   keys: ('runs', 1, 'name')
value: 0                                        keys: ('runs', 1, 'passed_count')
value: None                                     keys: ('runs', 1, 'plan_id')
value: 1                                        keys: ('runs', 1, 'project_id')
value: None                                     keys: ('runs', 1, 'refs')
value: 0                                        keys: ('runs', 1, 'retest_count')
value: 1                                        keys: ('runs', 1, 'suite_id')
value: 3                                        keys: ('runs', 1, 'untested_count')
value: 1650966329                               keys: ('runs', 1, 'updated_on')
value: https://xxxxxxxxxx.testrail.io/index.php?/runs/view/9 keys: ('runs', 1, 'url')
value: 2                                        keys: ('size',)
https://stackoverflow.com/questions/73708706/how-to-get-values-from-list-of-nested-dictionaries/73839430#73839430
before:
{'results': [{'end_time': '2021-01-21',
              'key': 'q1',
              'result_type': 'multipleChoice',
              'start_time': '2021-01-21',
              'value': ['1']},
             {'end_time': '2021-01-21',
              'key': 'q2',
              'result_type': 'multipleChoice',
              'start_time': '2021-01-21',
              'value': ['False']},
             {'end_time': '2021-01-21',
              'key': 'q3',
              'result_type': 'multipleChoice',
              'start_time': '2021-01-21',
              'value': ['3']},
             {'end_time': '2021-01-21',
              'key': 'q4',
              'result_type': 'multipleChoice',
              'start_time': '2021-01-21',
              'value': ['3']}]}
Let's flatten it: flatten_nested_something_to_list_of_tuples(data)
value: q1                                       keys: ('results', 0, 'key')
value: 1                                        keys: ('results', 0, 'value')
value: 2021-01-21                               keys: ('results', 0, 'end_time')
value: 2021-01-21                               keys: ('results', 0, 'start_time')
value: multipleChoice                           keys: ('results', 0, 'result_type')
value: q2                                       keys: ('results', 1, 'key')
value: False                                    keys: ('results', 1, 'value')
value: 2021-01-21                               keys: ('results', 1, 'end_time')
value: 2021-01-21                               keys: ('results', 1, 'start_time')
value: multipleChoice                           keys: ('results', 1, 'result_type')
value: q3                                       keys: ('results', 2, 'key')
value: 3                                        keys: ('results', 2, 'value')
value: 2021-01-21                               keys: ('results', 2, 'end_time')
value: 2021-01-21                               keys: ('results', 2, 'start_time')
value: multipleChoice                           keys: ('results', 2, 'result_type')
value: q4                                       keys: ('results', 3, 'key')
value: 3                                        keys: ('results', 3, 'value')
value: 2021-01-21                               keys: ('results', 3, 'end_time')
value: 2021-01-21                               keys: ('results', 3, 'start_time')
value: multipleChoice                           keys: ('results', 3, 'result_type')
https://stackoverflow.com/questions/70811820/pandas-multiindex-from-nested-dictionary
before:
{'A': [1, 2],
 'B': [2, 3],
 'Coords': [{'X': [1, 2, 3], 'Y': [1, 2, 3], 'Z': [1, 2, 3]},
            {'X': [2, 3], 'Y': [2, 3], 'Z': [2, 3]}]}
Let's flatten it: flatten_nested_something_to_list_of_tuples(data)
value: 1                                        keys: ('A',)
value: 2                                        keys: ('A',)
value: 2                                        keys: ('B',)
value: 3                                        keys: ('B',)
value: 1                                        keys: ('Coords', 0, 'X')
value: 2                                        keys: ('Coords', 0, 'X')
value: 3                                        keys: ('Coords', 0, 'X')
value: 1                                        keys: ('Coords', 0, 'Y')
value: 2                                        keys: ('Coords', 0, 'Y')
value: 3                                        keys: ('Coords', 0, 'Y')
value: 1                                        keys: ('Coords', 0, 'Z')
value: 2                                        keys: ('Coords', 0, 'Z')
value: 3                                        keys: ('Coords', 0, 'Z')
value: 2                                        keys: ('Coords', 1, 'X')
value: 3                                        keys: ('Coords', 1, 'X')
value: 2                                        keys: ('Coords', 1, 'Y')
value: 3                                        keys: ('Coords', 1, 'Y')
value: 2                                        keys: ('Coords', 1, 'Z')
value: 3                                        keys: ('Coords', 1, 'Z')
https://stackoverflow.com/questions/72017771/key-error-when-accessing-a-nested-dictionary
before:
[{'blocks': [{'block_id': 'BJNTn',
              'text': {'text': 'You have a new message.',
                       'type': 'mrkdwn',
                       'verbatim': False},
              'type': 'section'},
             {'block_id': 'WPn/l',
              'text': {'text': '*Heard By*\nFriend',
                       'type': 'mrkdwn',
                       'verbatim': False},
              'type': 'section'},
             {'block_id': '5yp',
              'text': {'text': '*Which Direction? *\nNorth',
                       'type': 'mrkdwn',
                       'verbatim': False},
              'type': 'section'},
             {'block_id': 'fKEpF',
              'text': {'text': '*Which Destination*\nNew York',
                       'type': 'mrkdwn',
                       'verbatim': False},
              'type': 'section'},
             {'block_id': 'qjAH',
              'text': {'text': '*New Customer:*\\Yes',
                       'type': 'mrkdwn',
                       'verbatim': False},
              'type': 'section'},
             {'block_id': 'yt4',
              'elements': [{'action_id': '+bc',
                            'text': {'bar': 'View results',
                                     'emoji': True,
                                     'type': 'plain_text'},
                            'type': 'button',
                            'url': 'www.example.com/results'}],
              'type': 'actions'},
             {'block_id': 'IBr',
              'text': {'text': ' ', 'type': 'mrkdwn', 'verbatim': False},
              'type': 'section'}],
  'bot_id': 'BPD4K3SJW',
  'subtype': 'bot_message',
  'text': "This content can't be displayed.",
  'timestamp': '1650905606.755969',
  'type': 'message',
  'username': 'admin'},
 {'blocks': [{'block_id': 'Smd',
              'text': {'text': 'You have a new message.',
                       'type': 'mrkdwn',
                       'verbatim': False},
              'type': 'section'},
             {'block_id': '6YaLt',
              'text': {'text': '*Heard By*\nOnline Search',
                       'type': 'mrkdwn',
                       'verbatim': False},
              'type': 'section'},
             {'block_id': 'w3o',
              'text': {'text': '*Which Direction: *\nNorth',
                       'type': 'mrkdwn',
                       'verbatim': False},
              'type': 'section'},
             {'block_id': 'PTQ',
              'text': {'text': '*Which Destination? *\nMiami',
                       'type': 'mrkdwn',
                       'verbatim': False},
              'type': 'section'},
             {'block_id': 'JCfSP',
              'text': {'text': '*New Customer? *\nNo',
                       'type': 'mrkdwn',
                       'verbatim': False},
              'type': 'section'},
             {'block_id': 'yt4',
              'elements': [{'action_id': '+bc',
                            'text': {'bar': 'View results',
                                     'emoji': True,
                                     'type': 'plain_text'},
                            'type': 'button',
                            'url': 'www.example.com/results'}],
              'type': 'actions'},
             {'block_id': 'RJOA',
              'text': {'text': ' ', 'type': 'mrkdwn', 'verbatim': False},
              'type': 'section'}],
  'bot_id': 'BPD4K3SJW',
  'subtype': 'bot_message',
  'text': "This content can't be displayed.",
  'timestamp': '1650899428.077709',
  'type': 'message',
  'username': 'admin'}]
Let's flatten it: flatten_nested_something_to_list_of_tuples(data)
value: message                                  keys: (0, 'type')
value: bot_message                              keys: (0, 'subtype')
value: This content can't be displayed.         keys: (0, 'text')
value: 1650905606.755969                        keys: (0, 'timestamp')
value: admin                                    keys: (0, 'username')
value: BPD4K3SJW                                keys: (0, 'bot_id')
value: section                                  keys: (0, 'blocks', 0, 'type')
value: BJNTn                                    keys: (0, 'blocks', 0, 'block_id')
value: mrkdwn                                   keys: (0, 'blocks', 0, 'text', 'type')
value: You have a new message.                  keys: (0, 'blocks', 0, 'text', 'text')
value: False                                    keys: (0, 'blocks', 0, 'text', 'verbatim')
value: section                                  keys: (0, 'blocks', 1, 'type')
value: WPn/l                                    keys: (0, 'blocks', 1, 'block_id')
value: mrkdwn                                   keys: (0, 'blocks', 1, 'text', 'type')
value: *Heard By*
Friend                        keys: (0, 'blocks', 1, 'text', 'text')
value: False                                    keys: (0, 'blocks', 1, 'text', 'verbatim')
value: section                                  keys: (0, 'blocks', 2, 'type')
value: 5yp                                      keys: (0, 'blocks', 2, 'block_id')
value: mrkdwn                                   keys: (0, 'blocks', 2, 'text', 'type')
value: *Which Direction? *
North                keys: (0, 'blocks', 2, 'text', 'text')
value: False                                    keys: (0, 'blocks', 2, 'text', 'verbatim')
value: section                                  keys: (0, 'blocks', 3, 'type')
value: fKEpF                                    keys: (0, 'blocks', 3, 'block_id')
value: mrkdwn                                   keys: (0, 'blocks', 3, 'text', 'type')
value: *Which Destination*
New York             keys: (0, 'blocks', 3, 'text', 'text')
value: False                                    keys: (0, 'blocks', 3, 'text', 'verbatim')
value: section                                  keys: (0, 'blocks', 4, 'type')
value: qjAH                                     keys: (0, 'blocks', 4, 'block_id')
value: mrkdwn                                   keys: (0, 'blocks', 4, 'text', 'type')
value: *New Customer:*\Yes                      keys: (0, 'blocks', 4, 'text', 'text')
value: False                                    keys: (0, 'blocks', 4, 'text', 'verbatim')
value: actions                                  keys: (0, 'blocks', 5, 'type')
value: yt4                                      keys: (0, 'blocks', 5, 'block_id')
value: button                                   keys: (0, 'blocks', 5, 'elements', 0, 'type')
value: +bc                                      keys: (0, 'blocks', 5, 'elements', 0, 'action_id')
value: plain_text                               keys: (0, 'blocks', 5, 'elements', 0, 'text', 'type')
value: View results                             keys: (0, 'blocks', 5, 'elements', 0, 'text', 'bar')
value: True                                     keys: (0, 'blocks', 5, 'elements', 0, 'text', 'emoji')
value: www.example.com/results                  keys: (0, 'blocks', 5, 'elements', 0, 'url')
value: section                                  keys: (0, 'blocks', 6, 'type')
value: IBr                                      keys: (0, 'blocks', 6, 'block_id')
value: mrkdwn                                   keys: (0, 'blocks', 6, 'text', 'type')
value:                                          keys: (0, 'blocks', 6, 'text', 'text')
value: False                                    keys: (0, 'blocks', 6, 'text', 'verbatim')
value: message                                  keys: (1, 'type')
value: bot_message                              keys: (1, 'subtype')
value: This content can't be displayed.         keys: (1, 'text')
value: 1650899428.077709                        keys: (1, 'timestamp')
value: admin                                    keys: (1, 'username')
value: BPD4K3SJW                                keys: (1, 'bot_id')
value: section                                  keys: (1, 'blocks', 0, 'type')
value: Smd                                      keys: (1, 'blocks', 0, 'block_id')
value: mrkdwn                                   keys: (1, 'blocks', 0, 'text', 'type')
value: You have a new message.                  keys: (1, 'blocks', 0, 'text', 'text')
value: False                                    keys: (1, 'blocks', 0, 'text', 'verbatim')
value: section                                  keys: (1, 'blocks', 1, 'type')
value: 6YaLt                                    keys: (1, 'blocks', 1, 'block_id')
value: mrkdwn                                   keys: (1, 'blocks', 1, 'text', 'type')
value: *Heard By*
Online Search                 keys: (1, 'blocks', 1, 'text', 'text')
value: False                                    keys: (1, 'blocks', 1, 'text', 'verbatim')
value: section                                  keys: (1, 'blocks', 2, 'type')
value: w3o                                      keys: (1, 'blocks', 2, 'block_id')
value: mrkdwn                                   keys: (1, 'blocks', 2, 'text', 'type')
value: *Which Direction: *
North                keys: (1, 'blocks', 2, 'text', 'text')
value: False                                    keys: (1, 'blocks', 2, 'text', 'verbatim')
value: section                                  keys: (1, 'blocks', 3, 'type')
value: PTQ                                      keys: (1, 'blocks', 3, 'block_id')
value: mrkdwn                                   keys: (1, 'blocks', 3, 'text', 'type')
value: *Which Destination? *
Miami              keys: (1, 'blocks', 3, 'text', 'text')
value: False                                    keys: (1, 'blocks', 3, 'text', 'verbatim')
value: section                                  keys: (1, 'blocks', 4, 'type')
value: JCfSP                                    keys: (1, 'blocks', 4, 'block_id')
value: mrkdwn                                   keys: (1, 'blocks', 4, 'text', 'type')
value: *New Customer? *
No                      keys: (1, 'blocks', 4, 'text', 'text')
value: False                                    keys: (1, 'blocks', 4, 'text', 'verbatim')
value: actions                                  keys: (1, 'blocks', 5, 'type')
value: yt4                                      keys: (1, 'blocks', 5, 'block_id')
value: button                                   keys: (1, 'blocks', 5, 'elements', 0, 'type')
value: +bc                                      keys: (1, 'blocks', 5, 'elements', 0, 'action_id')
value: plain_text                               keys: (1, 'blocks', 5, 'elements', 0, 'text', 'type')
value: View results                             keys: (1, 'blocks', 5, 'elements', 0, 'text', 'bar')
value: True                                     keys: (1, 'blocks', 5, 'elements', 0, 'text', 'emoji')
value: www.example.com/results                  keys: (1, 'blocks', 5, 'elements', 0, 'url')
value: section                                  keys: (1, 'blocks', 6, 'type')
value: RJOA                                     keys: (1, 'blocks', 6, 'block_id')
value: mrkdwn                                   keys: (1, 'blocks', 6, 'text', 'type')
value:                                          keys: (1, 'blocks', 6, 'text', 'text')
value: False                                    keys: (1, 'blocks', 6, 'text', 'verbatim')
https://stackoverflow.com/questions/73643077/how-to-transform-a-list-of-nested-dictionaries-into-a-data-frame-pd-json-normal
before:
[{'apple': {'price': 4, 'units': 3}},
 {'banana': {'price': 2, 'units': 20}},
 {'orange': {'price': 5, 'units': 15}}]
Let's flatten it: flatten_nested_something_to_list_of_tuples(data)
value: 3                                        keys: (0, 'apple', 'units')
value: 4                                        keys: (0, 'apple', 'price')
value: 20                                       keys: (1, 'banana', 'units')
value: 2                                        keys: (1, 'banana', 'price')
value: 15                                       keys: (2, 'orange', 'units')
value: 5                                        keys: (2, 'orange', 'price')
https://stackoverflow.com/questions/58110440/opening-nested-dict-in-a-single-column-to-multiple-columns-in-pandas
before:
{'simple25b': {'hands': {'0': {'currency': 'rm',
                               'handId': 'xyz',
                               'time': '2019-09-23 11:00:01'},
                         '1': {'currency': 'rm',
                               'handId': 'abc',
                               'time': '2019-09-23 11:01:18'}}},
 'simple5af': {'hands': {'0': {'currency': 'rm',
                               'handId': 'akg',
                               'time': '2019-09-23 10:53:22'},
                         '1': {'currency': 'rm',
                               'handId': 'mzc',
                               'time': '2019-09-23 10:54:15'},
                         '2': {'currency': 'rm',
                               'handId': 'swk',
                               'time': '2019-09-23 10:56:03'},
                         '3': {'currency': 'rm',
                               'handId': 'pQc',
                               'time': '2019-09-23 10:57:15'},
                         '4': {'currency': 'rm',
                               'handId': 'ywh',
                               'time': '2019-09-23 10:58:53'}}}}
Let's flatten it: flatten_nested_something_to_list_of_tuples(data)
value: xyz                                      keys: ('simple25b', 'hands', '0', 'handId')
value: 2019-09-23 11:00:01                      keys: ('simple25b', 'hands', '0', 'time')
value: rm                                       keys: ('simple25b', 'hands', '0', 'currency')
value: abc                                      keys: ('simple25b', 'hands', '1', 'handId')
value: 2019-09-23 11:01:18                      keys: ('simple25b', 'hands', '1', 'time')
value: rm                                       keys: ('simple25b', 'hands', '1', 'currency')
value: akg                                      keys: ('simple5af', 'hands', '0', 'handId')
value: 2019-09-23 10:53:22                      keys: ('simple5af', 'hands', '0', 'time')
value: rm                                       keys: ('simple5af', 'hands', '0', 'currency')
value: mzc                                      keys: ('simple5af', 'hands', '1', 'handId')
value: 2019-09-23 10:54:15                      keys: ('simple5af', 'hands', '1', 'time')
value: rm                                       keys: ('simple5af', 'hands', '1', 'currency')
value: swk                                      keys: ('simple5af', 'hands', '2', 'handId')
value: 2019-09-23 10:56:03                      keys: ('simple5af', 'hands', '2', 'time')
value: rm                                       keys: ('simple5af', 'hands', '2', 'currency')
value: pQc                                      keys: ('simple5af', 'hands', '3', 'handId')
value: 2019-09-23 10:57:15                      keys: ('simple5af', 'hands', '3', 'time')
value: rm                                       keys: ('simple5af', 'hands', '3', 'currency')
value: ywh                                      keys: ('simple5af', 'hands', '4', 'handId')
value: 2019-09-23 10:58:53                      keys: ('simple5af', 'hands', '4', 'time')
value: rm                                       keys: ('simple5af', 'hands', '4', 'currency')
https://stackoverflow.com/questions/62059970/how-can-i-convert-nested-dictionary-to-pd-dataframe-faster
before:
{'file': 'name',
 'main': [{'answer': [{'comment': 'It is defined as',
                       'user': 'John',
                       'value': [{'my_value': 5, 'value_2': 10},
                                 {'my_value': 24, 'value_2': 30}]},
                      {'comment': 'as John said above it simply means',
                       'user': 'Sam',
                       'value': [{'my_value': 9, 'value_2': 10},
                                 {'my_value': 54, 'value_2': 19}]}],
           'closed': 'no',
           'question': 'what is ?',
           'question_no': 'Q.1'}]}
Let's flatten it: flatten_nested_something_to_list_of_tuples(data)
value: name                                     keys: ('file',)
value: Q.1                                      keys: ('main', 0, 'question_no')
value: what is ?                                keys: ('main', 0, 'question')
value: John                                     keys: ('main', 0, 'answer', 0, 'user')
value: It is defined as                         keys: ('main', 0, 'answer', 0, 'comment')
value: 5                                        keys: ('main', 0, 'answer', 0, 'value', 0, 'my_value')
value: 10                                       keys: ('main', 0, 'answer', 0, 'value', 0, 'value_2')
value: 24                                       keys: ('main', 0, 'answer', 0, 'value', 1, 'my_value')
value: 30                                       keys: ('main', 0, 'answer', 0, 'value', 1, 'value_2')
value: Sam                                      keys: ('main', 0, 'answer', 1, 'user')
value: as John said above it simply means       keys: ('main', 0, 'answer', 1, 'comment')
value: 9                                        keys: ('main', 0, 'answer', 1, 'value', 0, 'my_value')
value: 10                                       keys: ('main', 0, 'answer', 1, 'value', 0, 'value_2')
value: 54                                       keys: ('main', 0, 'answer', 1, 'value', 1, 'my_value')
value: 19                                       keys: ('main', 0, 'answer', 1, 'value', 1, 'value_2')
value: no                                       keys: ('main', 0, 'closed')
https://stackoverflow.com/questions/39634369/4-dimensional-nested-dictionary-to-pandas-data-frame
before:
{'orders': [{'created_at': '2016-09-20T22:04:49+02:00',
             'email': 'test@aol.com',
             'id': 4314127108,
             'line_items': [{'destination_location': {'address1': 'Teststreet '
                                                                  '12',
                                                      'address2': '',
                                                      'city': 'Berlin',
                                                      'country_code': 'DE',
                                                      'id': 2383331012,
                                                      'name': 'Test Test',
                                                      'zip': '10117'},
                             'gift_card': False,
                             'name': 'Blueberry Cup'},
                            {'destination_location': {'address1': 'Teststreet '
                                                                  '12',
                                                      'address2': '',
                                                      'city': 'Berlin',
                                                      'country_code': 'DE',
                                                      'id': 2383331012,
                                                      'name': 'Test Test',
                                                      'zip': '10117'},
                             'gift_card': False,
                             'name': 'Strawberry Cup'}]}]}
Let's flatten it: flatten_nested_something_to_list_of_tuples(data)
value: 2016-09-20T22:04:49+02:00                keys: ('orders', 0, 'created_at')
value: test@aol.com                             keys: ('orders', 0, 'email')
value: 4314127108                               keys: ('orders', 0, 'id')
value: Teststreet 12                            keys: ('orders', 0, 'line_items', 0, 'destination_location', 'address1')
value:                                          keys: ('orders', 0, 'line_items', 0, 'destination_location', 'address2')
value: Berlin                                   keys: ('orders', 0, 'line_items', 0, 'destination_location', 'city')
value: DE                                       keys: ('orders', 0, 'line_items', 0, 'destination_location', 'country_code')
value: 2383331012                               keys: ('orders', 0, 'line_items', 0, 'destination_location', 'id')
value: Test Test                                keys: ('orders', 0, 'line_items', 0, 'destination_location', 'name')
value: 10117                                    keys: ('orders', 0, 'line_items', 0, 'destination_location', 'zip')
value: False                                    keys: ('orders', 0, 'line_items', 0, 'gift_card')
value: Blueberry Cup                            keys: ('orders', 0, 'line_items', 0, 'name')
value: Teststreet 12                            keys: ('orders', 0, 'line_items', 1, 'destination_location', 'address1')
value:                                          keys: ('orders', 0, 'line_items', 1, 'destination_location', 'address2')
value: Berlin                                   keys: ('orders', 0, 'line_items', 1, 'destination_location', 'city')
value: DE                                       keys: ('orders', 0, 'line_items', 1, 'destination_location', 'country_code')
value: 2383331012                               keys: ('orders', 0, 'line_items', 1, 'destination_location', 'id')
value: Test Test                                keys: ('orders', 0, 'line_items', 1, 'destination_location', 'name')
value: 10117                                    keys: ('orders', 0, 'line_items', 1, 'destination_location', 'zip')
value: False                                    keys: ('orders', 0, 'line_items', 1, 'gift_card')
value: Strawberry Cup                           keys: ('orders', 0, 'line_items', 1, 'name')
```

```python
#The code that I used
from pprint import pprint
def print__(data_, stacklink,original_):
    print(stacklink)
    print(f'before:')
    pprint(original_)
    print('\nLet\'s flatten it: flatten_nested_something_to_list_of_tuples(data)\n')
    for value, keys in data_:
        print(f'value: {str(value).ljust(40)} keys: {keys}')
    print('\n\n\n')
```
