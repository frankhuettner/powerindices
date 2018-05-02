"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
https://github.com/frankhuettner/powerindices
"""

from setuptools import setup, find_packages
from codecs import open
# from os import path

# here = path.abspath(path.dirname(__file__))

# # Get the long description from the README file
# with open(path.join(here, 'README.md'), encoding='utf-8') as f:
#     long_description_from_md ='\n' + f.read()

long_description = """
It's cumbersome to manage multiple readme files, so please go to the [GitHub page](https://github.com/frankhuettner/powerindices) for further information. 
"""

setup(
    name='powerindices',  

    version='1.0.2',  

    description='This package computes the following powerindices for weighted voting games: Penrose Banzhaf index, Shapley Shubik index, and Coleman Shapley index.',  # Required

    long_description=long_description, #Pypi and markdown for documentation is seems complicated. So please find details in this readme [this readme](https://github.com/frankhuettner/powerindices/blob/master/README.md) 

    long_description_content_type='text/markdown',

    url='https://github.com/frankhuettner/powerindices',  

    author='Frank Huettner',  

    author_email='info@frankhuettner.de', 

    classifiers=[  

        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Science/Research',
        
        'Topic :: Sociology',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',

        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='Shapley value Shapley Shubik index Banzhaf Penrose Coleman Power index computation',  # Optional

    py_modules=["powerindices"], 

    project_urls={  # Optional
        'Source': 'https://github.com/frankhuettner/powerindices/',
    },
)
