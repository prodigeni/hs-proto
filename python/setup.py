#!/usr/bin/env python

__version__ = 8311

import os
from distutils.core import setup

packages = [x[0] for x in os.walk("hsproto")]

setup(
	name="hsproto",
	packages=packages,
	description="Python Protobuf files for Hearthstone",
	url="https://github.com/HearthSim/hs-proto",
	version=str(__version__),
)
