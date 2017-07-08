#!/usr/bin/env python

from distutils.core import setup

description = """Flask+VueJS+SemanticUI+Docker CLI helper.
Also, see https://github.com/italomaia/flask-vue-semantic-docker."""

setup(
    name='fvsd',
    version='1.0',
    description=description,
    author='Italo Maia',
    author_email='italo.maia@gmail.com',
    url='https://github.com/italomaia/fvsd-cli',
    scripts=['fvsd.py'],
)
