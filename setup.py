import os


from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

requires = [
    'requests>=2.7.0',
    'six>=1.9.0'
]

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
    classifiers=classifiers
)
