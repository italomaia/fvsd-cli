#!/usr/bin/env python

from distutils.core import setup

description = """Flask+VueJS+SemanticUI+Docker CLI helper.
Also, see https://github.com/italomaia/flask-vue-semantic-docker."""

setup(
    name='fvsd',
    version='1.0',
    description=description,
    author='Italo Maia',
    url='https://github.com/italomaia/fvsd-cli',
    install_requires=[],
    scripts=['fvsd.py'],
)
