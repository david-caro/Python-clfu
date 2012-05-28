#!/usr/bin/env python
#
# Copyright 2012 David Caro
#
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 3, as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#

import sys
import glob
from distutils.core import setup

setup(  name = 'python-clfu',
        version = '0.1',
        description = 'Commandlinefu.com API python library',
        author = 'David Caro',
        author_email = 'david.cari.estevez@gmail.com',
        py_modules = ['clfu', 'executor'],
        scripts = ['bin/clfu'],
        )
