import operator
from functools import reduce
from typing import Any, Generator, Union
from collections import defaultdict
from random import randrange
from random import choice

nested_dict = lambda: defaultdict(nested_dict)


class Tuppsub(tuple):
    """Protects tuples internally from being flattened, same as ProtectedTuple"""

    pass


class ProtectedTuple(tuple):
    """Protects tuples from being flattened, same as Tuppsub"""

    pass


class ProtectedList(list):
    """Protects lists from being flattened"""

    pass


class ProtectedDict(dict):
    """Protects dicts from being flattened"""

    pass


class ProtectedSet(set):
    """Protects sets from being flattened"""

    pass


def aa_flatten_dict_tu(
        v: dict,
        listitem: tuple,
        forbidden: tuple = (list, tuple, set, frozenset),
        allowed: tuple = (
                str,
                int,
                float,
                complex,
                bool,
                bytes,
                type(None),
                ProtectedTuple,
                ProtectedList,
                ProtectedDict,
                ProtectedSet,
                Tuppsub,
        ),
) -> Generator:
    """
    Flattens any dict, but should not be used directly, use fla_tu
    Use this function to flatten any iterable
        Parameters:
            v: dict
                Input dict
            listitem: tuple
                Keep track of dict keys
            forbidden: tuple
                Data dtype which cannot be returned
                (default=(list, tuple, set, frozenset))
            allowed: tuple
                Data dtype which can be returned
                default (
                str,
                int,
                float,
                complex,
                bool,
                bytes,
                type(None),
                ProtectedTuple,  # Inherits from tuple but is protected, this is how you protected iterables
                ProtectedList,  # same here
                ProtectedDict, # same here
                ProtectedSet, # same here
                Tuppsub  #Inherit from tuple and exclude it from being flattened -

                )
        Returns:
            Generator


    """

    if (
            isinstance(v, dict)
            or (hasattr(v, "items") and hasattr(v, "keys"))
            and not isinstance(v, allowed)
    ):  # we check right away if it is a dict or something similar (with keys/items). If we miss something, we will
        # only get the keys back.
        for k, v2 in v.items():
            newtu = listitem + (k,)  # we accumulate all keys in a tuple
            if isinstance(v2, allowed):
                yield Tuppsub((v2, newtu))
            # and check if there are more dicts (nested) in this dict
            else:
                yield from aa_flatten_dict_tu(
                    v2, listitem=newtu, forbidden=forbidden, allowed=allowed
                )
    elif isinstance(v, forbidden) and not isinstance(
            v, allowed
    ):  # if we have an iterable without keys (list, tuple, set, frozenset) we have to enumerate them to be able to
        # access the original dict values later: di['blabla'][0] instead of di['blabla']

        for indi, v2 in enumerate(v):

            if isinstance(v2, allowed):
                yield Tuppsub((v2, (listitem + (indi,))))
            #  if the value is not in our allowed data types, we have to check if it is an iterable
            else:
                yield from aa_flatten_dict_tu(
                    v2,
                    listitem=(listitem + (indi,)),
                    forbidden=forbidden,
                    allowed=allowed,
                )
    elif isinstance(v, allowed):
        #  if the datatype is allowed, we yield it
        yield Tuppsub((v, listitem))

    # Brute force to check if we have an iterable. We have to get all iterables!
    else:
        try:
            for indi2, v2 in enumerate(v):

                try:
                    if isinstance(v2, allowed):
                        yield Tuppsub((v2, (listitem + (indi2,))))

                    else:
                        yield aa_flatten_dict_tu(
                            v2,
                            listitem=(listitem + (indi2,)),
                            forbidden=forbidden,
                            allowed=allowed,
                        )
                except Exception:
                    # if there is an exception, it is probably not an iterable, so we yield it
                    yield Tuppsub((v2, listitem))
        except Exception:
            # if there is an exception, it is probably not an iterable, so we yield it
            yield Tuppsub((v, listitem))


def fla_tu(
        item: Any,
        walkthrough:
        tuple = (),  # accumulate nested keys / don't pass anything here unless you know what you are doing
        forbidden: tuple = (
                list,
                tuple,
                set,
                frozenset,
        ),  # forbidden to yield, need to be flattened
        allowed: tuple = (  # Data types we don't want to touch!
                str,
                int,
                float,
                complex,
                bool,
                bytes,
                type(None),
                ProtectedTuple,  #
                ProtectedList,
                ProtectedDict,
                ProtectedSet,
                Tuppsub  # This is the secret - Inherit from tuple and exclude it from being flattened -
                # ProtectedTuple does the same thing
        ),
        dict_variation=(
        # we don't check with isinstance(), rather with type(), that way we don't have to import collections.
                "collections.defaultdict",
                "collections.UserDict",
                "collections.OrderedDict",
        ),
) -> Generator:
    """
    Use this function to flatten any iterable


    Here is an example
        from flatten_any_dict_iterable_or_whatsoever import flatten_nested_something_to_list_of_tuples,set_in_original_iter,get_from_original_iter, fla_tu

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
                       .........

        pprint(list(fla_tu(data)))

        Result
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
         ......


    If you want to protect certain iterables from beeing flattened, use:
    from flatten_any_dict_iterable_or_whatsoever import ProtectedList,ProtectedDict,ProtectedTuple

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


    pprint(list(fla_tu(data)))

    Result

        [({'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9}, ('level1', 't1', 's1')),
         (1, ('level1', 't1', 's2', 'col1')),
         (5, ('level1', 't1', 's2', 'col2')),
         (4, ('level1', 't1', 's2', 'col3')),
         (8, ('level1', 't1', 's2', 'col4')),
            .........
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
            .......
         (4, ('level2', 't1', 's2', 'col3')),
         (5, ('level2', 't1', 's2', 'col4')),
         (11, ('level2', 't1', 's3', 'col1')),
         ([8, 3, 5, 23, '342342'], ('level2', 't1', 's3', 'col2')),
         (2, ('level2', 't1', 's3', 'col3')),
         (13, ('level2', 't1', 's3', 'col4')),
         (5, ('level2', 't1', 's4', 'col1')),
         (4, ('level2', 't1', 's4', 'col2')),
            .........
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
            ......


        Parameters:
            item: Any
                Input iterable
                Most of the time you will be using only this parameter.

            walkthrough: Union[tuple,None]
                If you use this parameter, you will probably change the order of the keys,
                that means, it is better not to use it.
                (default =None)
            forbidden: tuple
                Data dtype which cannot be returned
                (default=(list, tuple, set, frozenset))
            allowed: tuple
                Data dtype which can be returned
                default (
                str,
                int,
                float,
                complex,
                bool,
                bytes,
                type(None),
                ProtectedTuple,  # Inherits from tuple but is protected, this is how you protected iterables
                ProtectedList,  # same here
                ProtectedDict, # same here
                ProtectedSet, # same here
                Tuppsub  #Inherit from tuple and exclude it from being flattened -

                )
            dict_variation: tuple
                Due to recent changes, might not be necessary anymore, used to filter dict variations
                (default =
                (
                "collections.defaultdict",
                "collections.UserDict",
                "collections.OrderedDict",
                )
        Returns:
            Generator

    """
    if isinstance(item, allowed):  # allowed items, so let's yield them
        yield Tuppsub((item, (walkthrough,)))
    elif isinstance(item, forbidden) and not isinstance(item, allowed):
        for ini, xaa in enumerate(item):
            if not isinstance(xaa, allowed):
                try:
                    yield from fla_tu(
                        xaa,
                        walkthrough=(walkthrough + (ini,)),
                        forbidden=forbidden,
                        allowed=allowed,
                        dict_variation=dict_variation,
                    )  # if we have an iterable, we check recursively for other iterables

                except Exception:

                    yield Tuppsub(
                        (xaa, (walkthrough + (ini,)))
                    )  # we just yield the value (value, (key1,key2,...))  because it is probably not an iterable
            else:
                yield Tuppsub((xaa, (walkthrough + (ini,))))
    elif isinstance(
            item, dict
    ):  # we need to pass dicts to aa_flatten_dict_tu(), they need a special treatment, if not, we only get the keys from the dict back
        if not isinstance(item, allowed):
            yield from aa_flatten_dict_tu(
                item, listitem=walkthrough, forbidden=forbidden, allowed=allowed
            )
        else:
            yield Tuppsub((item, (walkthrough,)))
            # let's try to catch all different dict variations by using ( hasattr(item, "items") and hasattr(item, "keys").
    # If we dont pass it to aa_flatten_dict_tu(), we only get the keys back.
    #
    # -> (hasattr(item, "items") and hasattr(item, "keys") -> Maybe better here:     elif isinstance( item, dict ):
    elif (str(type(item)) in dict_variation) or (
            hasattr(item, "items") and hasattr(item, "keys")
    ):
        if not isinstance(item, allowed):
            yield from aa_flatten_dict_tu(
                dict(item), listitem=walkthrough, forbidden=forbidden, allowed=allowed
            )
        else:
            yield Tuppsub((item, (walkthrough,)))
    # isinstance(item, pd.DataFrame) maybe better?
    elif "DataFrame" in str(type(item)):

        yield from aa_flatten_dict_tu(
            item.to_dict(),
            # pandas needs to be converted to dict first, if not, we only get the columns back. Copying might not be necessary
            listitem=walkthrough,
            forbidden=forbidden,
            allowed=allowed,

        )

    # # many iterables are hard to identify using isinstance() / type(), so we have to use brute force to check if it is
    # an iterable. If one iterable escapes, we are screwed!
    else:
        try:
            for ini2, xaa in enumerate(item):
                try:
                    if isinstance(xaa, allowed):  # yield only for allowed data types

                        yield Tuppsub(
                            (xaa, (walkthrough + (ini2,)))
                        )  # yields (value, (key1,key2,...)) -> always same format -> first value, then all keys in another tuple
                    else:  # if it is not in the allowed data types, we check recursively for other iterables
                        yield from fla_tu(
                            xaa,
                            walkthrough=(
                                (walkthrough + (ini2,))
                            ),  # yields (value, (key1,key2,...))
                            forbidden=forbidden,
                            allowed=allowed,
                            dict_variation=dict_variation,
                        )
                except Exception:

                    yield Tuppsub(
                        (xaa, (walkthrough + (ini2,)))
                    )  # in case of an exception, we yield  (value, (key1,key2,...))
        except Exception:

            yield Tuppsub(
                (item, (walkthrough,))
            )  # in case of an exception, we yield  (value, (key1,key2,...))


def get_from_original_iter(iterable: Any, keys: Union[list, tuple]) -> Any:
    """
        # https://stackoverflow.com/a/14692747/15096247

    After having flattened the iterable using fla_tu(), you will have a list of tuples:

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

    You can use now:

    value_directly_from_original_iterable = get_from_original_iter(iterable=data, keys=('level1', 't1', 's1', 'col1'))
    Out[6]: 5

    to access the values.



        Parameters:
            iterable: Any
                The "original" iterable that you passed to fla_tu
            keys: Union[list,tuple]
                The keys as a list/tuple of your original iterable that you want to get
        Returns:
            Any

    """
    return reduce(operator.getitem, keys, iterable)


def set_in_original_iter(iterable: Any, keys: Union[list, tuple], value: Any) -> None:
    """
        # https://stackoverflow.com/a/14692747/15096247

    After having flattened the iterable using fla_tu(), you will have a list of tuples:

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

    You can use now:

    set_in_original_iter(iterable=data, keys=('level1', 't1', 's1', 'col1'), value=1000000000000000000)
    data
    Out[8]:
    {'level1': {'t1': {'s1': {'col1': 1000000000000000000,
        'col2': 4,
        'col3': 4,
        'col4': 9},
       's2': {'col1': 1, 'col2': 5, 'col3': 4, 'col4': 8},
       's3': {'col1': 11, 'col2': 8, 'col3': 2, 'col4': 9},
       's4': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9}},

    to change the value in your original iterable!

    THIS FUNCTION RETURNS >>>NONE<<<
    BECAUSE IT CHANGES THE ORIGINAL ITERABLE!
    BE CAREFUL WHAT YOU ARE DOING!!

    If you still need the original data, use:

    from copy import deepcopy
    data2 = deepcopy(data)
    list(fla_tu(data))
    set_in_original_iter(iterable=data, keys=('level1', 't1', 's1', 'col1'), value=1000000000000000000)
    data will be changed
    data2 remains unchanged

        Parameters:
            iterable: Any
                The "original" iterable that you passed to fla_tu.
                Should work with all MUTEABLE iterables
            keys: Union[list,tuple]
                The keys as a list/tuple of your original iterable that you want to get

            value: Any
                The value you want to set

        Returns:
            None

    """
    # https://stackoverflow.com/a/14692747/15096247
    get_from_original_iter(iterable, keys[:-1])[keys[-1]] = value


def flatten_nested_something_to_list_of_tuples(nested_whatever) -> list[tuple]:
    """
    Same as list(fla_tu(iterable))

        Parameters:
            nested_whatever: Any
        Returns:
            list[tuple]

    """
    return list(fla_tu(nested_whatever))


def create_random_dict(
        length: int = 50,
        min_depth: int = 100,
        max_depth: int = 300,
        keyrandrange: tuple = (1, 20000),
        valuepicklist: Union[list, None] = None,
) -> defaultdict:
    """
    Create random nested dicts for testing

    Example

        ab=create_random_dict(length = 3,min_depth=3, max_depth=6,valuepicklist=[55,5469,'sfdsdf'])

        Out[7]:  #it looks strange, but it works like a regular dict

        defaultdict(<function flatten_any_dict_iterable_or_whatsoever.<lambda>()>,
                    {'10340': defaultdict(<function flatten_any_dict_iterable_or_whatsoever.<lambda>()>,
                                 {'17542': defaultdict(<function flatten_any_dict_iterable_or_whatsoever.<lambda>()>,
                                              {'5555': defaultdict(<function flatten_any_dict_iterable_or_whatsoever.<lambda>()>,
                                                           {'12003': 'sfdsdf'})})}),
                     '4320': defaultdict(<function flatten_any_dict_iterable_or_whatsoever.<lambda>()>,
                                 {'16079': defaultdict(<function flatten_any_dict_iterable_or_whatsoever.<lambda>()>,
                                              {'849': defaultdict(<function flatten_any_dict_iterable_or_whatsoever.<lambda>()>,
                                                           {'9913': defaultdict(<function flatten_any_dict_iterable_or_whatsoever.<lambda>()>,
                                                                        {'11066': 5469})})})}),
                     '13358': defaultdict(<function flatten_any_dict_iterable_or_whatsoever.<lambda>()>,
                                 {'6811': defaultdict(<function flatten_any_dict_iterable_or_whatsoever.<lambda>()>,
                                              {'16722': defaultdict(<function flatten_any_dict_iterable_or_whatsoever.<lambda>()>,
                                                           {'4634': 'sfdsdf'})})})})

        Parameters:
            length:
                how many top-level keys
                (default = 50)
            min_depth:
                minimal depth of dict
                (default = 100)
            max_depth:
                maximal depth of dict
                (default = 300)
            keyrandrange:
                range for random.randrange to get arbitrary keys
                (default = (1,20000))
            valuepicklist:
                list of values that will be chosen randomly
                If None, a random number between 1 and 100 will be chosen
                (default = None)
        Returns:
            defaultdict
    """
    nesti = nested_dict()
    for x in range(length):
        keys = [
            str(randrange(*keyrandrange))
            for _ in range(randrange(min_depth, max_depth))
        ]
        if valuepicklist is None:
            get_from_original_iter(nesti, keys[:-1])[keys[-1]] = randrange(1, 100)
        else:
            get_from_original_iter(nesti, keys[:-1])[keys[-1]] = choice(valuepicklist)

    return nesti
