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

CSI: a paper soon available by Andre Casajus and Frank Huettner


## Examples
The example.py offers some examples, e.g. the powerindices for the UN Security Council. To this end, the quota is set to 39 and the weights are [7, 7, 7, 7, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], where the veto powers have 7 and the nonpermanent members have weight 1. 

Also, the powerindices for the EU Council can be computed computable: the quota is 65% of the population and the weight of every country is the population of this country. Moreover, the minimal size of a winning coalition must be specified: setting minimalWinningCoalitionSize=16 ensures that only coalitions with at least 16 members (i.e., 55% of the countries) are winning.


## Installation
0) If you haven't installed python yet, get it from https://www.anaconda.com/download/. After installation, you can start the application Spyder which is a convinient tool to start with. 
1) No installation of the powerindices package is necessary. Just copy powerindices.py to your workfolder and use the command `import powerindices`. For instance, if you have the example.py file in the same directory as the powerindices.py file, you can just run example.py. In the example.py, you further see how to call the functions that compute the indices.


## Requirements
numpy

math

## Used algorithm
We use an algorithm following that counts the number of swings of a voter, see e.g.,
> S. Kurz: Computing the Power Distribution in the IMF ([arXiv](http://arxiv.org/abs/1603.01443))
and the adaptation to the CSI discribed in our paper.

A simple modification for if the minimal size of a winning coalition is specified allows us to be more efficient, e.g. for calculating the EU Council power distribution.

## Author
[Frank Huettner](http:www.frankhuettner.de)
