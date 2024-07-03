# Merges multiple nested dicts without deleting any values (values with same keys are stored in lists)

```python
pip install dict-merger-keep-all
```

```python

from pprint import pprint as pp
from dict_merger_keep_all import dict_merger

people = {
    1: {"name": "John", "age": "27", "sex": "Male"},
    2: {"name": "Marie", "age": "22", "sex": "Female"},
    3: {"name": "Luna", "age": "24", "sex": "Female"},
    4: {
        "name": "Peter",
        "age": "29",
        "sex": ["Female", "Male"],
        1: "xx",
        "sex2": ("Female", "Male"),
    },
}

people3 = {
    1: {"namexxxxxxxxx": "John", "age": "27", "sex": "Male"},
    2: {"name": "Marie", "age": "22", "sex": "Female"},
    3: {"name": "Luna", "agexxxxxxxxxx": "24", "sex": "Female"},
    4: {
        "name": "Peter",
        "age": "29",
        "sex": ["Female", "Male"],
        1: "xx",
        "sex2": ("Female", "Male"),
    },
}
people2 = {
    11: {"name": "Johnaaa", "age": "2x337", "sex": "Maleooo"},
    21: {"name": "Mariexx", "age": "22", "sex": "Female"},
    13: {"name": "Luna", "age": "24444", "sex": "Feoomale"},
    14: {
        "name": "Peter",
        "age": "29",
        "sex": ["Female", "Male"],
        111: "xx",
        "sex2": ("Female", "Male"),
    },
}
d1 = {1: {"a": "A"}, 2: {"b": "B"}}

d2 = {2: {"c": "C"}, 3: {"d": ["D", "dd", "s"]}}

dict1 = {1: {"a": 1}, 2: {"b": 2}}

dict2 = {2: {"c": 222}, 3: {"d": {3, 6}}}


data = {
    "A": [1, 2, 3],
    "B": [4, 5, 6],
    "departure": [
        {
            "actual": None,
            "actual_runway": None,
            "airport": "Findel",
            "delay": None,
            "estimated": "2020-07-07T06:30:00+00:00",
            "estimated_runway": None,
            "gate": None,
            "iata": "LUX",
            "icao": "ELLX",
            "scheduled": "2020-07-07T06:30:00+00:00",
            "terminal": None,
            "timezone": "Europe/Luxembourg",
        },
        {
            "actual": None,
            "actual_runway": None,
            "airport": "Findel",
            "delay": None,
            "estimated": "2020-07-07T06:30:00+00:00",
            "estimated_runway": None,
            "gate": None,
            "iata": "LUX",
            "icao": "ELLX",
            "scheduled": "2020-07-07T06:30:00+00:00",
            "terminal": None,
            "timezone": "Europe/Luxembourg",
        },
        {
            "actual": None,
            "actual_runway": None,
            "airport": "Findel",
            "delay": None,
            "estimated": "2020-07-07T06:30:00+00:00",
            "estimated_runway": None,
            "gate": None,
            "iata": "LUX",
            "icao": "ELLX",
            "scheduled": "2020-07-07T06:30:00+00:00",
            "terminal": None,
            "timezone": "Europe/Luxembourg",
        },
    ],
}

data2 = {"A": [4, 5, 6]}

newdict = dict_merger(people, people2, d1, d2, dict2, dict1, data, data2, people3)
pp(newdict)



{1: {'a': ['A', 1],
     'age': ['27', '27'],
     'name': 'John',
     'namexxxxxxxxx': 'John',
     'sex': ['Male', 'Male']},
 2: {'age': ['22', '22'],
     'b': ['B', 2],
     'c': ['C', 222],
     'name': ['Marie', 'Marie'],
     'sex': ['Female', 'Female']},
 3: {'age': '24',
     'agexxxxxxxxxx': '24',
     'd': ['D', 'dd', 's', 3, 6],
     'name': ['Luna', 'Luna'],
     'sex': ['Female', 'Female']},
 4: {1: ['xx', 'xx'],
     'age': ['29', '29'],
     'name': ['Peter', 'Peter'],
     'sex': ['Female', 'Male', 'Female', 'Male'],
     'sex2': ['Female', 'Male', 'Female', 'Male']},
 11: {'age': '2x337', 'name': 'Johnaaa', 'sex': 'Maleooo'},
 13: {'age': '24444', 'name': 'Luna', 'sex': 'Feoomale'},
 14: {111: 'xx',
      'age': '29',
      'name': 'Peter',
      'sex': ['Female', 'Male'],
      'sex2': ['Female', 'Male']},
 21: {'age': '22', 'name': 'Mariexx', 'sex': 'Female'},
 'A': [1, 2, 3, 4, 5, 6],
 'B': [4, 5, 6],
 'departure': {0: {'actual': None,
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
               1: {'actual': None,
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
               2: {'actual': None,
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
                   'timezone': 'Europe/Luxembourg'}}}


```
