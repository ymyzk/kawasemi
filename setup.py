#!/usr/bin/env python
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

requires = [
    'Django>=1.7,<1.9',
    'requests>=2.7.0',
    'six>=1.9.0'
]

extras_require = {
    'docs': [
        'Sphinx<1.4,>=1.3',
        'sphinx-rtd-theme<0.2,>=0.1.8'
    ]
}

classifiers = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP',
]

setup(
    name='django-channels',
    version='0.1.0',
    packages=['channels'],
    include_package_data=True,
    license='MIT',
    description='',
    long_description=README,
    url='https://github.com/ymyzk/django-channels',
    author='Yusuke Miyazaki',
    author_email='miyazaki.dev@gmail.com',
    install_requires=requires,
    extras_require=extras_require,
    classifiers=classifiers
)
