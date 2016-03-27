=====
iface
=====

*Implementable interfaces for Python.*

Defining An interface
=====================

.. code-block:: python

    import iface

    class UserInterface(iface.Iface):

        """Interface for a user of the system."""

        @iface.classmethod
        def load(self, identifier):
            """Load a user object based on the DB identifier."""
            raise NotImplementedError()

        @iface.method
        def save(self):
            """Save the current user record to the DB."""
            raise NotImplementedError()

Interfaces definitions are subclasses of `Iface` that have some number of
attributes defined and decorated. Currently, the following kinds of attributes
are supported::

    -   attribute

        A named attribute that that contains any value.

    -   property

        A named attribute that is implemented as a property.

    -   classattribute

        A named attribute that is attached to the class rather than an instance.

    -   method

        A named attribute that is callable. Can be implemented as an instance
        method, class method, or static method.

    -   classmethod

        A named attribute that is callable and implemented as a class method.

Implementing An Interface
=========================

.. code-block:: python

    class User:

        """A user of the system."""

        @classmethod
        def load(cls, identifier):
            return cls()

        def save(self):
            return None

Unlike Java-style interfaces, no explicit binding needs to be made between the
implementation and definition of an interface. As long as an object has all the
right attributes defined it is considered an implementation. Implementations
don't need to import or use `iface` in any way.

Checking Implementations
========================

.. code-block:: python

    def do_something_with_user(user):
        assert isinstance(user, UserInterface)

The `isinstance` and `issubclass` built-ins can be used to verify if an object
implements a given interface. Using the built-ins performs a fairly naive check
that ensures the object has attributes that match all of the names defined in
the interface.

Additionally, this package provides alternative implementations of these
functions in the form of `iface.isinstance` and `iface.issubclass` that will
perform a more thorough inspection of the object and match against things like
class methods and class attributes.

The suggested pattern for checking implementations is to use the `assert`
statement. The assertion will raise an exception during testing and development
if the wrong objects are getting passed around. Before running in a production
like environment, use the use the `-O` flag or `PYTHONOPTIMIZE=1` environment
variable to strip out the assert statements and remove the cost of all the
attribute checking.

Testing
=======

All tests suites are paired one-to-one with the module they test and live
directly adjacent to that same module. All tests are expected to pass for
Python 3.3 and above. To run tests use tox with the included tox.ini file or
create a virtualenv and install the '[testing]' extras.

License
=======

    Copyright 2015 Kevin Conway

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

Contributing
============

Firstly, if you're putting in a patch then thank you! Here are some tips for
getting your patch merged:

Style
-----

As long as the code passes the PEP8 and PyFlakes gates then the style is
acceptable.

Docs
----

The PEP257 gate will check that all public methods have docstrings. If you're
adding something new, like a helper function, try out the
`napoleon style of docstrings <https://pypi.python.org/pypi/sphinxcontrib-napoleon>`_.

Tests
-----

Make sure the patch passes all the tests. If you're adding a new feature don't
forget to throw in a test or two. If you're fixing a bug then definitely add
at least one test to prevent regressions.
