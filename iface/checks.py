"""Extensions of isinstance and issubclass."""

from . import ibc

_issubclass = issubclass
_isinstance = isinstance


def _ensure_ifaces_tuple(ifaces):
    """Convert to a tuple of interfaces and raise if not interfaces."""
    try:

        ifaces = tuple(ifaces)

    except TypeError:

        ifaces = (ifaces,)

    for iface in ifaces:

        if not _issubclass(iface, ibc.Iface):

            raise TypeError('Can only compare against interfaces.')

    return ifaces


def _check_for_definition(iface, cls, tag, defines):
    """Check for a valid definition of a value.

    Args:
        iface (Iface): An Iface specification.
        cls (type): Some type to check for a definition.
        tag (str): The name of the tag attribute used to mark the abstract
            methods.
        defines (callable): A callable that accepts an attribute and returns
            True if the attribute is a valid definition.

    Returns:
        bool: Whether or not the definition is found.
    """
    attributes = (
        attr
        for attr in iface.__abstractmethods__
        if hasattr(getattr(iface, attr), tag)
    )
    for attribute in attributes:

        for node in cls.__mro__:

            if hasattr(node, attribute) and defines(getattr(node, attribute)):

                return True

    try:

        attribute
        return False

    except NameError:

        # Pass the test if the loop was never executed. This indicates there
        # were no iface elements defined in the search.
        return True


def _is_attribute(attr):
    """Return True if attr is an attribute."""
    return True


def _is_property(attr):
    """Return True if attr is a property."""
    return callable(attr) and _isinstance(attr, property)


def _is_method(attr):
    """Return True if attr is a method."""
    return callable(attr) or _isinstance(attr, (classmethod, staticmethod))


def _is_classmethod(attr):
    """Return True if attr is a classmethod."""
    return (
        callable(attr) and
        hasattr(attr, '__self__') and
        attr.__self__ is not None
    )


def issubclass(cls, ifaces):
    """Check if the given class is an implementation of the given iface."""
    ifaces = _ensure_ifaces_tuple(ifaces)
    for iface in ifaces:

        return all((
            _check_for_definition(
                iface,
                cls,
                '__iclassattribute__',
                _is_attribute,
            ),
            _check_for_definition(
                iface,
                cls,
                '__iproperty__',
                _is_property,
            ),
            _check_for_definition(
                iface,
                cls,
                '__imethod__',
                _is_method,
            ),
            _check_for_definition(
                iface,
                cls,
                '__iclassmethod__',
                _is_classmethod,
            ),
        ))


def isinstance(instance, ifaces):
    """Check if a given instance is an implementation of the interface."""
    ifaces = _ensure_ifaces_tuple(ifaces)
    for iface in ifaces:

        attributes = (
            attr
            for attr in iface.__abstractmethods__
            if hasattr(getattr(iface, attr), '__iattribute__')
        )
        for attribute in attributes:

            if not hasattr(instance, attribute):

                return False

        if not issubclass(type(instance), ifaces):

            return False

    return True
