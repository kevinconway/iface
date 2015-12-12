=====
iface
=====

*Implementable interfaces for Python.*

Example Usage
=============

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
