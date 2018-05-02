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
This [example.py](https://github.com/frankhuettner/powerindices/blob/master/example.py) offers some examples. 
### The powerindices for the UN Security Council
Here, the quota is set to 39 and 

the weights are [7, 7, 7, 7, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 

where the veto powers have 7 and the nonpermanent members have weight 1. 

Alternatively, set quota = 5, weights = [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0] and minimalWinningCoalitionSize=16.

### The powerindices for the EU Council 
Can be computed as well: the quota is 65% of the population and the weight of every country is the population of this country. Moreover, the minimal size of a winning coalition must be specified: setting `minimalWinningCoalitionSize=16` ensures that only coalitions with at least 16 members (i.e., 55% of the countries) are winning.

## Installation
If you haven't installed python yet, get it, e.g. from https://www.anaconda.com/download/. 

*Option 1)* It's just one file, so installation of the powerindices package necessary: 
..* Just download and copy powerindices.py and example.py into the same folder. 
..* Open example.py, e.g. using the application *Spyder* that comes with *Anaconda*.
..* There you see how the command `import powerindices` allows to use the functions to compute the indices if powerindices.py is in the same folder. If you run the example.py, it will run the computation for the UN Security Council.

*Option 2)* To install the tool, run `pip install powerindices` in your terminal. If you use anaconda, run the command in the [Anaconda Promt](https://www.quora.com/How-do-I-start-the-anaconda-command-prompt).

## Usage
After installation, you can start the application Spyder which is a convinient tool to start with. A video tutorial is coming soon. 

## Usage from within R
You can use this tool from within R by help of [reticulate](https://github.com/rstudio/reticulate). To this end,
* Install the package *powerindices* in your python environment running the command `pip install powerindices` in your terminal
* Install [reticulate](https://github.com/rstudio/reticulate) 
* call the package *powerindices* from within R and make sure to send integers, e.g., the following will store the CSIs for the UN Security Council in the list `csis
    ```
    library(reticulate)
    powi <- import("powerindices")
    csis <-powi$compute_csi(39L,c(7L, 7L, 7L, 7L, 7L, 1L, 1L, 1L, 1L, 1L, 1L, 1L, 1L, 1L, 1L))
    ```
## Requirements
You need to have numpy and math. I did not put it into the setup.py requirements because this seems to bring trouble. Both packages are standard and come with anaconda.

## Used algorithm
We use an algorithm following that counts the number of swings of a voter, see e.g.,
> S. Kurz: Computing the Power Distribution in the IMF ([arXiv](http://arxiv.org/abs/1603.01443))

> A. Casajus and F. Huettner: [The Coleman-Shapley-Index: Being Decisive Within the Coalition of the Interested'](http://xn--frankhttner-yhb.de/frankhuettner/wp-content/uploads/2018/05/colsha.pdf)

## Author
[Frank Huettner](http:www.frankhuettner.de)
