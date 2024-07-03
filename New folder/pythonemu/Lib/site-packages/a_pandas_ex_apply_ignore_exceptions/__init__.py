from functools import partial
import pandas as pd
from useful_functions_easier_life import ignore_exceptions_decorator
from pandas.core.frame import DataFrame, Series


def apply_i(
    df,
    exception_value,
    *args,
    print_exception=False,
    **kwargs,
):
    args1 = args[0]
    return df.apply(
        ignore_exceptions_decorator(
            partial(args1),
            exception_value=exception_value,
            disable=False,
            print_exception=print_exception,
        ),
        *args[1:],
        **kwargs,
    )


def pd_add_apply_ignore_exceptions():
    DataFrame.ds_apply_ignore = apply_i
    Series.ds_apply_ignore = apply_i


