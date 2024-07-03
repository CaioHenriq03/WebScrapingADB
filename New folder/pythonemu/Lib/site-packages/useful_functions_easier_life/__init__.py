from functools import partial, wraps

from decorator import decorator


class NamedFunction:
    """
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


    """

    def __init__(
        self,
        name="",
        execute_function=lambda: "",
        name_function=lambda: "",
        str_prefix="",
        str_suffix="",
        print_before_execution="",
        ljust_prefix=0,
        rjust_prefix=0,
        ljust_suffix=0,
        rjust_suffix=0,
    ):
        self.f = execute_function
        self.n = name_function
        self.str_prefix = str(str_prefix)
        self.str_suffix = str(str_suffix)

        self.name = self.str_prefix + str(name) + self.str_suffix
        self.ljust_prefix = ljust_prefix
        self.rjust_prefix = rjust_prefix
        self.ljust_suffix = ljust_suffix
        self.rjust_suffix = rjust_suffix
        self.print_before_execution = str(print_before_execution)

    def __call__(self, *args, **kwargs):
        print(self.print_before_execution, end="")
        return self.f(*args, **kwargs)

    def __str__(self):
        self.update_name()

        return self.name

    def __repr__(self):
        self.update_name()
        return self.name

    def update_name(self):
        self.name = NamedFunction.return_string(
            self.str_prefix.ljust(self.ljust_prefix).rjust(self.rjust_prefix)
            + str(self.n()).ljust(self.ljust_suffix).rjust(self.rjust_suffix)
            + self.str_suffix
        )

    @staticmethod
    def return_string(_):
        return str(_)


@decorator
def ignore_exceptions_decorator_simple(func, *args, **kwargs):
    exception_value = None
    try:
        return func(*args, **kwargs)
    except Exception:
        return exception_value


def ignore_exceptions(func, *args, **kwargs):
    """
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

    """

    if "exception_value" in kwargs:
        exception_value = kwargs["exception_value"]
        del kwargs["exception_value"]
    else:
        exception_value = None
    try:
        return func(*args, **kwargs)
    except Exception:
        return exception_value


def ignore_exceptions_decorator(
    f_py=None, print_exception=True, exception_value=None, disable=True
):
    """
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

    https://stackoverflow.com/questions/5929107/decorators-with-parameters

    #Blueprint for other useful stuff
    """
    assert callable(f_py) or f_py is None

    def _decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if disable is False:
                try:
                    return func(*args, **kwargs)
                except Exception as fexa:
                    if print_exception:
                        print(fexa)
                    return exception_value
            else:
                try:
                    return func(*args, **kwargs)
                except Exception as feba:
                    if print_exception:
                        print(feba)
                    if disable:
                        raise feba
                    return exception_value

        return wrapper

    return _decorator(f_py) if callable(f_py) else _decorator


def execute_several_functions_insideout(*decs):
    """
    ca2 = execute_several_functions_insideout(
        lambda x: x * 100, lambda x: x / 10, lambda x: x * 5, lambda x: x + 1000
    )

    ca2(5)
    Out[6]: 50250.0

    (1000+5) * 5 / 10 * 100
    Out[18]: 50250.0


    """

    @ignore_exceptions_decorator(print_exception=True, exception_value=None)
    def deco(f):
        for dec in reversed(decs):
            f = dec(f)
        return f

    return deco


def execute_several_functions_one_after_another(all_functions: list, arguments=True):
    """
    allfunctions=lambda x: (x, isinstance(x,str)),lambda x: str(x) + '-1000', lambda x:x*5, lambda x: isinstance(x,str)
    ca=execute_several_functions_one_after_another(allfunctions)


    ca(101)
    Out[4]: [(101, False), '101-1000', 505, False]
    """
    if arguments:
        return partial(join_functions, all_functions=all_functions)
    else:
        return partial(join_functions_noargs, all_functions=all_functions)


def join_functions_noargs(all_functions):
    lala = lambda: [xx() for xx in all_functions]
    return lala()


def join_functions(va, all_functions):
    lala = lambda: [xx(va) for xx in all_functions]
    return lala()
