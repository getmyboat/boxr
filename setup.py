from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='boxr',
    version='1.0.1',
    description='An Open Exchange Rate Client',
    long_description=long_description,
    url='https://github.com/getmyboat/boxr',
    author='GetMyBoat, LLC',
    author_email='alex@getmyboat.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='foreign exchange rates',
    packages=['boxr'],
    install_requires=['requests'],
    tests_require=['pytest'],
)
