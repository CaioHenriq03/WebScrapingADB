import operator
from collections import defaultdict
from functools import reduce
from tolerant_isinstance import isinstance_tolerant
from flatten_any_dict_iterable_or_whatsoever import fla_tu


def convert_to_normal_dict(di):
    if isinstance_tolerant(di, defaultdict):
        di = {k: convert_to_normal_dict(v) for k, v in di.items()}
    return di


nested_dict = lambda: defaultdict(nested_dict)


def dict_merger(*args):
    newdict = nested_dict()
    for it in args:
        for p in fla_tu(it):
            tcr = type(reduce(operator.getitem, p[1][:-1], it))
            if tcr is tuple or tcr is set:
                tcr = list
            if tcr == list:
                try:
                    if not reduce(operator.getitem, p[1][:-2], newdict)[p[1][-2]]:
                        reduce(operator.getitem, p[1][:-2], newdict)[p[1][-2]] = tcr()
                    reduce(operator.getitem, p[1][:-2], newdict)[p[1][-2]].append(
                         p[0]
                    )
                except Exception:
                    try:
                        reduce(operator.getitem, p[1][:-1], newdict)[p[1][-1]] = p[0]
                    except Exception:
                        reduce(operator.getitem, p[1][:-2], newdict)[p[1][-2]] = [
                            reduce(operator.getitem, p[1][:-1], newdict)[p[1][-1]],
                            p[0],
                        ]

            else:
                try:
                    if not reduce(operator.getitem, p[1][:-1], newdict)[p[1][-1]]:
                        reduce(operator.getitem, p[1][:-1], newdict)[p[1][-1]] = p[0]
                    else:
                        reduce(operator.getitem, p[1][:-1], newdict)[p[1][-1]] = [
                            reduce(operator.getitem, p[1][:-1], newdict)[p[1][-1]]
                        ]
                        reduce(operator.getitem, p[1][:-1], newdict)[p[1][-1]].append(
                            p[0]
                        )
                except Exception:
                    reduce(operator.getitem, p[1][:-2], newdict)[p[1][-2]] = [
                        reduce(operator.getitem, p[1][:-1], newdict)[p[1][-1]],
                        p[0],
                    ]
    return convert_to_normal_dict(newdict)
