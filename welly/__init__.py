#!/usr/bin/env python
# -*- coding: utf 8 -*-
"""
==================
welly
==================
"""
from .project import Project
from .well import Well
from .header import Header
from .curve import Curve
from .scorecard import Scorecard
from .synthetic import Synthetic
from .location import Location
from .crs import CRS
from . import tools

__all__ = [
           'Project',
           'Well',
           'Header',
           'Curve',
           'Scorecard',
           'Synthetic',
           'Location',
           'CRS',
           'tools',  # Various classes in here
          ]


__version__ = "unknown"
try:
    from ._version import __version__
except ImportError:
    pass
