#!/usr/bin/env python
from codecs import open
from os import path

from setuptools import find_packages, setup


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
    'test': [
        'pytest>=3.0.0,<4.0.0',
        'pytest-mock>=1.5.0,<2.0.0',
    ],
    'test:python_version < "3.3"': ['mock>=2.0.0,<3.0.0']
}

classifiers = [
    'Development Status :: 4 - Beta',
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
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Topic :: Internet :: WWW/HTTP',
]

setup(
    name='kawasemi',
    version='1.0.0b1',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    include_package_data=True,
    license='MIT',
    description='A Python library for sending notifications to services such as Slack, HipChat, Twitter, and so on',
    long_description=long_description,
    url='https://github.com/ymyzk/kawasemi',
    author='Yusuke Miyazaki',
    author_email='miyazaki.dev@gmail.com',
    install_requires=requires,
    extras_require=extras_require,
    classifiers=classifiers
)
