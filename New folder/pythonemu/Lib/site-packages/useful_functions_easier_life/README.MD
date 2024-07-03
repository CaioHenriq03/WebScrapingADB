#### Some useful stuff for functions

##### NamedFunction
```python
pip install useful-functions-easier-life
```

```python
    namedfunctiontest = NamedFunction(
        name="myfunction",
        execute_function=execute_several_functions_insideout(
            lambda x: x * 100, lambda x: x / 10, lambda x: x * 5, lambda x: x + 1000
        ),
        name_function=lambda: "This is my function",
        str_prefix="Surprise",
        print_before_execution="My function\n",
        str_suffix="Let's go!",
        ljust_prefix=10,
        rjust_prefix=30,
        ljust_suffix=20,
        rjust_suffix=10,
    )


    namedfunctiontest
    Out[3]:                     Surprise  This is my function Let's go!

    #Without namedfunction:
    #ca2
    #Out[7]: <function __main__.execute_several_functions_insideout.<locals>.deco(f)>

    namedfunctiontest(5)
    My function
    Out[6]: 50250.0
```

##### ignore_exceptions_decorator

```python
    from random import choice

    @ignore_exceptions_decorator(print_exception=True, exception_value=False, disable=False)
    def testest(number):
        if number == 0:
            return True
        elif number == 1:
            print(number / 0)
        return True


    testex = [testest(choice([0, 1])) for x in range(10)]


    division by zero
    division by zero
    testex
    Out[3]: [True, True, False, True, False, True, True, True, True, True]

    #https://stackoverflow.com/questions/5929107/decorators-with-parameters

    #Blueprint for other useful stuff
```

##### execute_several_functions_insideout

```python
    ca2 = execute_several_functions_insideout(
        lambda x: x * 100, lambda x: x / 10, lambda x: x * 5, lambda x: x + 1000
    )

    ca2(5)
    Out[6]: 50250.0

    (1000+5) * 5 / 10 * 100
    Out[18]: 50250.0
```

##### execute_several_functions_one_after_another

```python
    allfunctions=lambda x: (x, isinstance(x,str)),lambda x: str(x) + '-1000', lambda x:x*5, lambda x: isinstance(x,str)
    ca=execute_several_functions_one_after_another(allfunctions)


    ca(101)
    Out[4]: [(101, False), '101-1000', 505, False]
```

##### ignore_exceptions

```python
    testex = [ignore_exceptions(divmod, 50, choice([0, 1]),exception_value=(0,0)) for x in range(10)]

    testex
    Out[7]:
    [(50, 0),
     (0, 0),
     (0, 0),
     (0, 0),
     (50, 0),
     (50, 0),
     (50, 0),
     (50, 0),
     (50, 0),
     (0, 0)]
```
