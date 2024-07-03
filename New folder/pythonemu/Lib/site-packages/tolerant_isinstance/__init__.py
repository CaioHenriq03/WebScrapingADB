from isiter import isiter


def isinstance_tolerant(__object, __classinfo):
    if not isiter(__classinfo):
        __classinfo = [__classinfo]

    for modul in __classinfo:
        try:
            if isinstance(__object, modul):

                return True
        except Exception:
            pass
        try:
            if type(__object).__module__ == getattr(modul, "__name__"):
                return True
        except Exception:
            pass
        try:
            if str(type(__object)) == str(type(modul)):
                return True
        except Exception:
            pass
        return False
