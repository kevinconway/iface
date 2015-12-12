"""Test suites for the ibc module."""

import abc

from . import ibc


class IfaceTestClass(ibc.Iface):

    """An interface used for testing."""

    @abc.abstractmethod
    def some_method(self):
        """Do nothing."""
        return None

    @property
    @abc.abstractmethod
    def some_property(self):
        """Get nothing."""
        return None


class ImplementationAsClass:

    """IfaceTestClass implementation defined within a class."""

    def some_method(self):
        """Do nothing."""
        return None

    @property
    def some_property(self):
        """Get nothing."""
        return None


class ImplementationAsInstance:

    """IfaceTestClass implementation as a class instance."""

    def __init__(self):
        """Generate the some_property attribute."""
        self.some_property = None

    def some_method(self):
        """Do nothing."""
        return None


class ImplementationWithInheritanceBase:

    """IfaceTestClass implementation that uses inheritance."""

    def some_method(self):
        """Do nothing."""
        return None


class ImplementationWithInheritance(ImplementationWithInheritanceBase):

    """IfaceTestClass implementation that uses inheritance."""

    @property
    def some_property(self):
        """Get nothing."""
        return None


def test_subclass_fail():
    """Check that issubclass is False for non-implementations."""
    assert not issubclass(object, IfaceTestClass)


def test_instance_fail():
    """CHeck that isinstance is False for non-implementations."""
    assert not isinstance(object(), IfaceTestClass)


def test_subclass_full_impl():
    """Check issubclass for class defined implementation."""
    assert issubclass(ImplementationAsClass, IfaceTestClass)


def test_instance_full_impl():
    """Check isinstance for class defined implementations."""
    assert isinstance(ImplementationAsClass(), IfaceTestClass)


def test_subclass_inheritance():
    """Check issubclass for class defined with inheritance."""
    assert issubclass(ImplementationWithInheritance, IfaceTestClass)


def test_instance_inheritance():
    """Check isinstance for class defined with inheritance."""
    assert isinstance(ImplementationWithInheritance(), IfaceTestClass)


def test_instance_attributes():
    """Check isinstance for class using instance attributes."""
    assert isinstance(ImplementationAsInstance(), IfaceTestClass)
