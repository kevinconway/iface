"""Base interface functionality."""

import abc


class IfaceMeta(abc.ABCMeta):

    """ABCMeta extensions for deeper object inspection.

    This extensions builds on the existing __instancecheck__ method within the
    ABCMeta to allow inspection of attributes that are created during
    initialization rather than at class definition.

    To use this feature, interfaces using this metaclass can define a method
    named __instancehook__ which behaves similarly to __subclasshook__ except
    that it receives an instance of a class.
    """

    def __instancecheck__(cls, other):
        """Check if an instance implements the interface.

        This modification adds support for a new magic method called
        __instancehook__ that will be used to determine if an instance
        is an implementation. This method will be given one argument that
        is a reference to the instance being checked. If the hook returns
        NotImplemented then the standard __subclasshook__ method is called.
        """
        if hasattr(cls, '__instancehook__') and callable(cls.__instancehook__):

            result = cls.__instancehook__(other)
            if result is not NotImplemented:

                return result

        return abc.ABCMeta.__instancecheck__(cls, other)


class Iface(metaclass=IfaceMeta):

    """Base class from which all interfaces can extend.

    This basic implementation allows for subclasses to be used as the target of
    isinstance() and issubclass() calls. Using the interface this way will
    perform a lightweight inspection of the other object and return True if the
    other has, at least, all the same attribute names as those wrapped with
    abstractmethod in the interface definition.
    """

    @classmethod
    def __subclasshook__(cls, other):
        """Check if the other class implements the interface."""
        for attribute in cls.__abstractmethods__:

            if not any(
                hasattr(othercls, attribute)
                for othercls in other.__mro__
            ):

                return False

        return True

    @classmethod
    def __instancehook__(cls, other):
        """Check if the other instance implements the interface."""
        for attribute in cls.__abstractmethods__:

            if not hasattr(other, attribute):

                return NotImplemented

        return True
