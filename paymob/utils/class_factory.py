# Python Standard Library Imports


class BaseClass(object):
    def __init__(self, classtype):
        self._type = classtype


def ClassFactory(name, BaseClass=BaseClass):
    name = "".join(element.capitalize() for element in name.split("_"))

    def _wrap(key, value):
        if isinstance(value, (tuple, list, set, frozenset)):
            return type(value)([_wrap(key, v) for v in value])
        else:
            klass = ClassFactory(key)
            return klass(**value) if isinstance(value, dict) else value

    def __init__(self, **kwargs):

        for key, value in kwargs.items():
            # here, the argnames variable is the one passed to the
            # ClassFactory call
            setattr(self, key, _wrap(key, value))

        BaseClass.__init__(self, name[: -len("Class")])

    newclass = type(name, (BaseClass,), {"__init__": __init__})
    return newclass


__all__ = [ClassFactory]
