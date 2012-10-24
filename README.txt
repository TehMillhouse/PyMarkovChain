=============
PyMarkovChain
=============

PyMarkovChain supplies an easy-to-use implementation of a markov chain text generator.
To use it, you can simply do

    #!/usr/bin/env python

    from pymarkovchain import MarkovChain

    # To generate the markov chain's language model, in case it's not present
    MarkovChain().generateDatabase("This is some language to analyze")
    # To let the markov chain generate some text, execute
	MarkovChain().generateString()

To store its data, PyMarkovChain simply uses pickle to dump all of its data to disk.
This entails that you have to use the same version of python to store the data and to
restore the data, as pickle is one of those things that have changed from python2 to python3.

See also [code on github](https://github.com/MaxWagner/PyMarkovChain) and [PyPI page](http://pypi.python.org/pypi/PyMarkovChain/). To install, simply use pip like so:
    pip install PyMarkovChain
