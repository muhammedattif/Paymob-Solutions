# Python Standard Library Imports
from types import MethodType


class ClassUtils:
    @staticmethod
    def get_callables(old_cls):
        method_list = []

        # attribute is a string representing the attribute name
        for attribute in dir(old_cls):
            # Get the attribute value
            attribute_value = getattr(old_cls, attribute)
            # Check that it is callable
            if callable(attribute_value):
                # Filter all dunder (__ prefix) methods
                if attribute.startswith("__") == False:
                    method_list.append(attribute)
        return method_list

    @classmethod
    def set_callables(cls, old_cls, new_cls):

        callables = cls.get_callables(old_cls=old_cls)

        for cal in callables:
            setattr(new_cls, cal, MethodType(getattr(old_cls, cal), new_cls))

        return new_cls
