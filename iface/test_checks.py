"""Test suites for the checks module."""

from . import checks
from . import decorators
from . import ibc


def test_subclass_classattributes():
    """Check if class attributes are found by issubclass."""
    class IExample(ibc.Iface):

        """Example interface."""

        @decorators.classattribute
        def value(self):
            """Get a value."""
            return None

    class Example:

        """Example implementation."""

        value = None

    assert checks.issubclass(Example, IExample)


def test_subclass_method_instance():
    """Check if methods are found by issubclass when instancemethod."""
    class IExample(ibc.Iface):

        """Example interface."""

        @decorators.method
        def value(self):
            """Get a value."""
            return None

    class Example:

        """Example implementation."""

        def value(self):
            """Get a value."""
            return None

    assert checks.issubclass(Example, IExample)


def test_subclass_method_class():
    """Check if methods are found by issubclass when classmethod."""
    class IExample(ibc.Iface):

        """Example interface."""

        @decorators.method
        def value(self):
            """Get a value."""
            return None

    class Example:

        """Example implementation."""

        @classmethod
        def value(cls):
            """Get a value."""
            return None

    assert checks.issubclass(Example, IExample)


def test_subclass_method_static():
    """Check if methods are found by issubclass when staticmethod."""
    class IExample(ibc.Iface):

        """Example interface."""

        @decorators.method
        def value(self):
            """Get a value."""
            return None

    class Example:

        """Example implementation."""

        @staticmethod
        def value():
            """Get a value."""
            return None

    assert checks.issubclass(Example, IExample)


def test_subclass_method_value():
    """Check if methods are not found by issubclass when not a method."""
    class IExample(ibc.Iface):

        """Example interface."""

        @decorators.method
        def value(self):
            """Get a value."""
            return None

    class Example:

        """Example implementation."""

        value = None

    assert not checks.issubclass(Example, IExample)


def test_subclass_classmethod_value():
    """Check if classmethods are not found by issubclass when not a method."""
    class IExample(ibc.Iface):

        """Example interface."""

        @decorators.classmethod
        def value(cls):
            """Get a value."""
            return None

    class Example:

        """Example implementation."""

        value = None

    assert not checks.issubclass(Example, IExample)


def test_subclass_classmethod_static():
    """Check if classmethods are not found by issubclass when staticmethod."""
    class IExample(ibc.Iface):

        """Example interface."""

        @decorators.classmethod
        def value(cls):
            """Get a value."""
            return None

    class Example:

        """Example implementation."""

        @staticmethod
        def value():
            """Get a value."""
            return None

    assert not checks.issubclass(Example, IExample)


def test_subclass_classmethod_instance():
    """Check if classmethods are not found by issubclass when instance."""
    class IExample(ibc.Iface):

        """Example interface."""

        @decorators.classmethod
        def value(cls):
            """Get a value."""
            return None

    class Example:

        """Example implementation."""

        def value(self):
            """Get a value."""
            return None

    assert not checks.issubclass(Example, IExample)


def test_subclass_classmethod_class():
    """Check if classmethods are found by issubclass when classmethod."""
    class IExample(ibc.Iface):

        """Example interface."""

        @decorators.classmethod
        def value(cls):
            """Get a value."""
            return None

    class Example:

        """Example implementation."""

        @classmethod
        def value(cls):
            """Get a value."""
            return None

    assert checks.issubclass(Example, IExample)


def test_subclass_property_value():
    """Check if properties are not found by issubclass when values."""
    class IExample(ibc.Iface):

        """Example interface."""

        @decorators.property
        def value(self):
            """Get a value."""
            return None

    class Example:

        """Example implementation."""

        value = None

    assert not checks.issubclass(Example, IExample)


def test_instance_attribute():
    """Check if attributes are found by isinstance."""
    class IExample(ibc.Iface):

        """Example interface."""

        @decorators.attribute
        def value(self):
            """Get a value."""
            return None

    class Example:

        """Example implementation."""

        value = None

    assert checks.isinstance(Example, IExample)
