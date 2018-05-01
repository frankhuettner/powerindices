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
# powerindices
This package computes 
the Penrose Banzhaf index (PBI), 
the Shapley Shubik index (SSI), and 
the Coleman Shapley index (CSI)
for weighted voting games. 
Both, quota and weights must be **integers**.
Moreover, it is possible to give an optional arguemnent: the minimal size of a winning coalition.

For information about the indices:

PBI: https://en.wikipedia.org/wiki/Banzhaf_power_index

SSI: https://en.wikipedia.org/wiki/Shapley%E2%80%93Shubik_power_index

CSI: [The Coleman-Shapley-Index: Being Decisive Within the Coalition of the Interested](http://xn--frankhttner-yhb.de/frankhuettner/wp-content/uploads/2018/05/colsha.pdf) by [André Casajus](http:www.casajus.de) and [Frank Huettner](http:www.frankhuettner.de)


## Examples
This [example.py](https://github.com/frankhuettner/powerindices/blob/master/example.py) offers some examples, e.g. the powerindices for the UN Security Council. To this end, the quota is set to 39 and the weights are [7, 7, 7, 7, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], where the veto powers have 7 and the nonpermanent members have weight 1. 

Also, the powerindices for the EU Council can be computed computable: the quota is 65% of the population and the weight of every country is the population of this country. Moreover, the minimal size of a winning coalition must be specified: setting minimalWinningCoalitionSize=16 ensures that only coalitions with at least 16 members (i.e., 55% of the countries) are winning.


## Requirements
You need to have numpy and math. I did not put it into the setup requirements because this seems to bring trouble.


## Used algorithm
We use an algorithm following that counts the number of swings of a voter, see e.g.,
> S. Kurz: Computing the Power Distribution in the IMF ([arXiv](http://arxiv.org/abs/1603.01443))

> A. Casajus and F. Huettner: [The Coleman-Shapley-Index: Being Decisive Within the Coalition of the Interested'](http://xn--frankhttner-yhb.de/frankhuettner/wp-content/uploads/2018/05/colsha.pdf)


## Author
[Frank Huettner](http:www.frankhuettner.de)
"""

setup(
    name='powerindices',  

    version='1.0.0',  

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
