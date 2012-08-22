#!/usr/bin/env python
#
# setup.py -- Installation for rbtools.
#
# Copyright (C) 2009 Christian Hammond
# Copyright (C) 2009 David Trowbridge
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages
from setuptools.command.test import test

from rbtools import get_package_version


PACKAGE_NAME = 'YYReview'

setup(name=PACKAGE_NAME,
      version=get_package_version(),
      license="MIT",
      description="Command line tools for use with Review Board for YY",
      entry_points = {
          'console_scripts': [
              'yyreview = rbtools.postreview:main',
          ],
      },
      install_requires=[],
      dependency_links = [],
      packages=find_packages(),
      include_package_data=True,
      maintainer="Shaoyan Huang",
      maintainer_email="huangshaoyan1982@gmail.com",
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Environment :: Console",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Software Development",
      ]
)
