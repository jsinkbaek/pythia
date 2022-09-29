# pythia
# Author: Cole Johnston
# co-authors: Nora Eisner

## Contributors: Dominic Bowman

### Edited by Jeppe Sinkbæk Thomsen to be install-able using pip

Modules and routines for time-series analysis of astronomical data sets.


timeseries/periodograms -- library containing functions for time-series analysis


Can be installed using pip. From the base package directory (the one with folders src and test in, and files README.md and LICENSE), do:

`pip install .`

Make sure that the dependencies are functional beforehand. F.ex., that the correct version of theano-pymc is used for pymc3.
If you have problems with theano, try (in a terminal with your python environment sourced):

`pip uninstall theano`
`pip uninstall theano-pymc`
`pip install theano-pymc`


Be aware that the import statements are slightly different than before, as all the function files are in the root package folder.
So now, for example, importing LS_periodograms would be

`from pythia.periodograms import LS_periodograms`

instead of

`from pythia.timeseries.periodograms import LS_periodograms`

### TO DO:
  - Generalize handling of priors
  - Include GUI support
  - Include Gaussian Processes
  - Expand to multiple filters (long term)
