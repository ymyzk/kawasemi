#!/usr/bin/env python
from codecs import open
from os import path
import sys

from setuptools import setup


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

requires = [
    'requests>=2.7.0',
    'requests-oauthlib>=0.5.0',
    'six>=1.9.0'
]

extras_require = {
    ':python_version < "3.5"': ['typing'],
    'docs': [
        'Sphinx>=1.4,<1.5',
        'sphinx-rtd-theme>=0.1.9,<0.2'
    ],
    'test': []
}

# TODO: Replace with environment markers in the future
if sys.version_info < (3, 3):
    extras_require['test'].append('mock>=1.2.0')

classifiers = [
    'Development Status :: 3 - Alpha',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Topic :: Internet :: WWW/HTTP',
]

setup(
    name='django-channels',
    version='0.6.1',
    packages=['channels', 'channels.backends'],
    include_package_data=True,
    license='MIT',
    description='A Django library for sending notifications',
    long_description=long_description,
    url='https://github.com/ymyzk/django-channels',
    author='Yusuke Miyazaki',
    author_email='miyazaki.dev@gmail.com',
    install_requires=requires,
    extras_require=extras_require,
    classifiers=classifiers
)
