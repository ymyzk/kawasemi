#!/usr/bin/env python
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


__version__ = '0.3.0'

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

requires = [
    'requests>=2.7.0',
    'requests-oauthlib>=0.5.0',
    'six>=1.9.0'
]

extras_require = {
    'docs': [
        'Sphinx<1.4,>=1.3',
        'sphinx-rtd-theme<0.2,>=0.1.8'
    ],
    'test': []
}

if sys.version_info < (3, 3):
    extras_require['test'].append('mock>=1.0.1')

classifiers = [
    'Development Status :: 3 - Alpha',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Topic :: Internet :: WWW/HTTP',
]

setup(
    name='django-channels',
    version=__version__,
    packages=['channels', 'channels.backends'],
    include_package_data=True,
    license='MIT',
    description='A Django library for sending notifications',
    long_description=README,
    url='https://github.com/ymyzk/django-channels',
    author='Yusuke Miyazaki',
    author_email='miyazaki.dev@gmail.com',
    install_requires=requires,
    extras_require=extras_require,
    classifiers=classifiers
)
