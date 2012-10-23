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

Included in the package is a sample database called 'markovdb' (this is the name of the database this file uses), which was built from the script of Monkey Island games (for which I do *not* own the rights. The file's merely there for demonstration purposes, if the inclusion of this file is a problem, just tell me and I'll promptly remove it).
