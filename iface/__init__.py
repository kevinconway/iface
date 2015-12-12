"""Implementable interfaces for Python."""

from .checks import isinstance
from .checks import issubclass

from .decorators import attribute
from .decorators import property
from .decorators import classattribute
from .decorators import method
from .decorators import classmethod

from .ibc import Iface

__all__ = (
    'isinstance',
    'issubclass',
    'attribute',
    'property',
    'classattribute',
    'method',
    'classmethod',
    'Iface',
)
