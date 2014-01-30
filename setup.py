#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='pytest-django-lite',
    version='0.1.1',
    description='The bare minimum to integrate py.test with Django.',
    author='David Cramer',
    author_email='dcramer@gmail.com',
    url='https://github.com/dcramer/pytest-django-lite',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    long_description=open('README.rst').read(),
    license='Apache License 2.0',
    install_requires=[
        'pytest',
        'django>=1.2',
    ],
    # the following makes a plugin available to py.test
    entry_points={
        'pytest11': ['django = pytest_django_lite.plugin'],
    },
)
