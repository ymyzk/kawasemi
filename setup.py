#!/usr/bin/env python
from codecs import open
from os import path
import sys

from setuptools import find_packages, setup


here = path.abspath(path.dirname(__file__))

def get_version():
    about_file = path.join(here, 'kawasemi/__about__.py')
    if sys.version_info[0] >= 3:
        about = {}
        with open(about_file) as fp:
            exec(fp.read(), about)
        return about['__version__']
    else:
        execfile(about_file)
        return __version__

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

requires = [
    'click>=6.0,<7.0',
    'requests>=2.7.0',
    'requests-oauthlib>=0.5.0',
    'six>=1.9.0'
]

extras_require = {
    ':python_version < "3.5"': ['typing'],
    'docs': [
        'Sphinx>=1.6,<1.7',
        'sphinx-rtd-theme>=0.2,<0.3'
    ],
    'test': [
        'coverage>=4.3.4,<5.0.0',
        'coveralls>=1.1,<2.0',
        'flake8>=3.3.0,<4.0.0',
        'pytest>=3.0.0,<4.0.0',
        'pytest-cov>=2.4.0,<3.0.0',
        'pytest-mock>=1.5.0,<2.0.0',
    ],
    'test:python_version >= "3.3"': [
        'mypy',
    ],
}

classifiers = [
    'Development Status :: 5 - Production/Stable',
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

entry_points = {
    'console_scripts': [
        'kawasemi=kawasemi.cli:main',
    ],
}

setup(
    name='kawasemi',
    version=get_version(),
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
    entry_points=entry_points,
    classifiers=classifiers
)
