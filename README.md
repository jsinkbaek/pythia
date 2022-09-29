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

### TO DO:
  - Generalize handling of priors
  - Include GUI support
  - Include Gaussian Processes
  - Expand to multiple filters (long term)
