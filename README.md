=============
PyMarkovChain
=============

PyMarkovChain supplies an easy-to-use implementation of a markov chain text generator.  
To use it, you can simply do

    #!/usr/bin/env python

    from pymarkovchain import MarkovChain
    # Create an instance of the markov chain. By default, it uses MarkovChain.py's location to
    # store and load its database files to. You probably want to give it another location, like so:
    mc = MarkovChain("./markov")
    # To generate the markov chain's language model, in case it's not present
    mc.generateDatabase("This is a string of Text. It won't generate an interesting database though.")
    # To let the markov chain generate some text, execute
    mc.generateString()

To store its data, PyMarkovChain simply uses pickle to dump all of its data to disk.
This entails that you have to use the same version of python to store the data and to
restore the data, as pickle is one of those things that have changed from python2 to python3.

See also [code on github](https://github.com/MaxWagner/PyMarkovChain) and [PyPI page](http://pypi.python.org/pypi/PyMarkovChain/).
To install, simply use pip like so:
    pip install PyMarkovChain
