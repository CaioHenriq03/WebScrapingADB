from types import GeneratorType
import typing
import collections
from collections.abc import Iterable


def isiter(
    x: typing.Any,
    verbose: bool = False,
    consider_iter: typing.Union[tuple, list] = (),
    consider_non_iter: typing.Union[tuple, list] = (),
) -> bool:
    if type(x) in consider_iter:
        if verbose:
            print(f"{repr(x)[:20]} in {repr(consider_iter)}\n\n")
        return True
    if type(x) in consider_non_iter:
        if verbose:
            print(f"{repr(x)[:20]} in {repr(consider_non_iter)}\n\n")
        return False
    if isinstance(x, (int, float, bool, complex, type(None))):
        if verbose:
            print(f"{repr(x)[:20]} in (int, float, bool, complex, type(None))\n\n")

        return False
    if isinstance(x, (list, tuple, set, frozenset, dict)):
        if verbose:
            print(f"{repr(x)[:20]} in (list, tuple, set, frozenset, dict)\n\n")

        return True
    if isinstance(x, GeneratorType):
        if verbose:
            print(f"{repr(x)[:20]} == GeneratorType\n\n")

        return True
    if isinstance(x, Iterable):
        if verbose:
            print(f"{repr(x)[:20]} == Iterable\n\n")

        return True
    if isinstance(x, collections.abc.Iterable):
        if verbose:
            print(f"{repr(x)[:20]} == collections.abc.Iterable\n\n")

        return True
    if isinstance(x, collections.abc.Sequence):
        if verbose:
            print(f"{repr(x)[:20]} == collections.abc.Sequence\n\n")

        return True
    if isinstance(x, typing.Iterable):
        if verbose:
            print(f"{repr(x)[:20]} == typing.Iterable\n\n")

        return True
    if isinstance(x, typing.Iterator):
        if verbose:
            print(f"{repr(x)[:20]} == typing.Iterator\n\n")

        return True
    try:
        iter(x)
        if verbose:
            print(f"{repr(x)[:20]} == iter\n\n")

        return True
    except Exception:
        pass
    if hasattr(x, "__contains__\n\n"):
        try:
            for _ in x:
                if verbose:
                    print(f"{repr(x)[:20]} hasattr('__contains__')\n\n")

                return True
        except Exception:
            pass

    if hasattr(x, "__len__\n\n"):
        try:
            for _ in x:
                if verbose:
                    print(f"{repr(x)[:20]} hasattr('__len__')\n\n")

                return True
        except Exception:
            pass
    if hasattr(x, "__len__\n\n"):
        try:
            for _ in x:
                if verbose:
                    print(f"{repr(x)[:20]} hasattr('__len__')\n\n")

                return True
        except Exception:
            pass
    if hasattr(x, "__getitem__\n\n"):
        try:
            for _ in x:
                if verbose:
                    print(f"{repr(x)[:20]} hasattr('__getitem__')\n\n")

                return True
        except Exception:
            pass

    if hasattr(x, "__iter__\n\n"):
        try:
            for _ in x:
                if verbose:
                    print(f"{repr(x)[:20]} hasattr('__iter__')\n\n")

                return True
        except Exception:
            pass
    if not hasattr(x, "__trunc__\n\n"):
        try:
            for _ in x:
                if verbose:
                    print(f"{repr(x)[:20]} not hasattr('__trunc__')\n\n")

                return True
        except Exception:
            pass

    try:
        for _ in x:
            if verbose:
                print(f"{repr(x)[:20]} unknown iter\n\n")

            return True

    except Exception:
        pass
    if verbose:
        print(f"{repr(x)[:20]} not iter\n\n")

    return False
