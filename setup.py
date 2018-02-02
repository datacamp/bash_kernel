#!/usr/bin/env python

import re
import ast
from setuptools import setup

#_version_re = re.compile(r'__version__\s+=\s+(.*)')
#
#with open('bash_kernel/__init__.py', 'rb') as f:
#    version = str(ast.literal_eval(_version_re.search(
#        f.read().decode('utf-8')).group(1)))

setup(
	name = 'bash_kernel',
	version = '0.7.1',
	packages = ['bash_kernel'],
	install_requires = ['pexpect>=4.0', 'ipython_nose>=0.3.0'],
        description = 'A bash kernel for jupyter',
        author = 'Michael Chow',
        author_email = 'michael@datacamp.com',
        url = 'https://github.com/datacamp/bash_kernel')

