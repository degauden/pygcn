# Copyright (C) 2014-2018  Leo Singer
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import ast
import sys
import os

from setuptools import setup
import versioneer

setup_requires = ['setuptools >= 30.3.0']
if {'pytest', 'test', 'ptr'}.intersection(sys.argv):
    setup_requires.append('pytest-runner')

# Get docstring and version without importing module
with open('gcn/__init__.py') as f:
    mod = ast.parse(f.read())
__doc__ = ast.get_docstring(mod)

user_install = False
for a in sys.argv:
    if a.startswith("--user"):
        user_install = True

systemd_target_dir = "/usr/lib/systemd/user"
if user_install:
    systemd_target_dir = os.environ["HOME"] + "/.local/share/systemd/user"

setup(description=__doc__.splitlines()[1],
      long_description=__doc__,
      setup_requires=setup_requires,
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      data_files=[(systemd_target_dir , ["data/systemd/pygcn.service"])])
