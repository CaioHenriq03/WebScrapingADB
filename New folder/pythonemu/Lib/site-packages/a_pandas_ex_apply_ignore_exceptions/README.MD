# Use DataFrame.apply / Series.apply with a default value for Exceptions 

```python
pip install a-pandas-ex-apply-ignore-exceptions
```

```python

from a_pandas_ex_apply_ignore_exceptions import pd_add_apply_ignore_exceptions
import pandas as pd
pd_add_apply_ignore_exceptions()
df = pd.read_csv(
    "https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv"
)

# the Exception value is the first arg, the rest is just like apply
df1 = df.PassengerId.ds_apply_ignore(pd.NA, lambda x: x / 3)
df2 = df.ds_apply_ignore(pd.NA, lambda x: x["PassengerId"] / 3, axis=1)
df3 = df.PassengerId.ds_apply_ignore(pd.NA, lambda x: x / 0)
df4 = df.ds_apply_ignore(pd.NA, lambda x: x["PassengerId"] / 0, axis=1)
print(df1)
print(df2)
print(df3)
print(df4)


r"""
0        0.333333
1        0.666667
2        1.000000
3        1.333333
4        1.666667
          ...    
886    295.666667
887    296.000000
888    296.333333
889    296.666667
890    297.000000
Name: PassengerId, Length: 891, dtype: float64
0        0.333333
1        0.666667
2        1.000000
3        1.333333
4        1.666667
          ...    
886    295.666667
887    296.000000
888    296.333333
889    296.666667
890    297.000000
Length: 891, dtype: float64
0      <NA>
1      <NA>
2      <NA>
3      <NA>
4      <NA>
       ... 
886    <NA>
887    <NA>
888    <NA>
889    <NA>
890    <NA>
Name: PassengerId, Length: 891, dtype: object
0      <NA>
1      <NA>
2      <NA>
3      <NA>
4      <NA>
       ... 
886    <NA>
887    <NA>
888    <NA>
889    <NA>
890    <NA>
Length: 891, dtype: object

"""

		
```