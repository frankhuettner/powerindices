"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
https://github.com/frankhuettner/powerindices
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='powerindices',  

    version='0.1',  

    description='This package computes the following powerindices for weighted voting games: Penrose Banzhaf index, Shapley Shubik index, and Coleman Shapley index.',  # Required

    long_description=long_description, 

    long_description_content_type='text/markdown',  

    url='https://github.com/frankhuettner/powerindices',  

    author='Frank Huettner',  

    author_email='info@frankhuettner.de', 

    classifiers=[  # Optional

        'Development Status :: 4 - Beta',

        'Intended Audience :: Researchers',
        
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Cooperative Game Theory',
        'Topic :: Scientific/Engineering :: Cooperative Game Theory :: Computation of Powerindices',

        'License :: OSI Approved :: Apache License 2.0',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='Shapley value Shapley Shubik index Banzhaf Penrose Coleman Power index computation',  # Optional

    py_modules=["powerindices"]), 

    install_requires=['numpy','math'],  

    project_urls={  # Optional
        'Source': 'https://github.com/frankhuettner/powerindices/',
    },
)
