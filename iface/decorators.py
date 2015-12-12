"""Method decorators that extend abc.abstractmethod."""

import abc


_classmethod = classmethod
_staticmethod = staticmethod
_property = property


class Property(_property):

    """Property subclass that adds the __iproperty__ attribute."""

    __iproperty__ = True


def attribute(func):
    """Wrap a function as an attribute."""
    attr = abc.abstractmethod(func)
    attr.__iattribute__ = True
    attr = _property(attr)
    return attr


def property(func):
    """Wrap a function as a property.

    This differs from attribute by identifying properties explicitly listed
    in the class definition rather than named attributes defined on instances
    of a class at init time.
    """
    attr = abc.abstractmethod(func)
    attr.__iproperty__ = True
    attr = Property(attr)
    return attr


def classattribute(func):
    """Wrap a function as a class attribute.

    This differs from attribute by identifying attributes explicitly listed
    in a class definition rather than those only defined on instances of
    a class.
    """
    attr = abc.abstractmethod(func)
    attr.__iclassattribute__ = True
    attr = _property(attr)
    return attr


def method(func):
    """Wrap a function as a method."""
    attr = abc.abstractmethod(func)
    attr.__imethod__ = True
    return attr


def classmethod(func):
    """Wrap a function as a classmethod.

    This applies the classmethod decorator.
    """
    attr = abc.abstractmethod(func)
    attr.__iclassmethod__ = True
    attr = _classmethod(attr)
    return attr
