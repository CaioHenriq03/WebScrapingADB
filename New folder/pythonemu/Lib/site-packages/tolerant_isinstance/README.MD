# isinstance - more tolerant 

```python
# Tested with:
# Python 3.9.13
# Windows 10

This function checks: 
isinstance(__object, modul)
type(__object).__module__ == getattr(modul, "__name__")
str(type(__object)) == str(type(modul))


p = pd.NA
isinstance(p, pd.NA) # Exception
isinstance_tolerant(p, pd.NA) # no Exception
p = None
isinstance(p, None) # Exception
isinstance_tolerant(p, None)  # no Exception


```



