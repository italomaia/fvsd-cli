#!/usr/bin/env python

import sys
from distutils.core import setup

long_description = """
Using the repository (https://github.com/italomaia/flask-vue-semantic-docker),
this CLI is capable of easely creating a boilerplate project using
Flask, VueJS, Nginx, SemanticUI and Docker in a easy manner.

Just install this package and call fvsd.py new <project-name> to get started.
""".strip()

required = []

if sys.version_info.major == 3:
    required.append('fabric3')
else:
    required.append('fabric')


setup(
    name='fvsd',
    version='1.0.4',
    description="Flask+VueJS+SemanticUI+Docker CLI boilerplate.",
    long_description=long_description,
    author='Italo Maia',
    author_email='italo.maia@gmail.com',
    url='https://github.com/italomaia/fvsd-cli',
    scripts=['fvsd.py'],
    install_requires=required,
)
