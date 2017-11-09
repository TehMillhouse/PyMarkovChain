
PyMarkovChain
=============

PyMarkovChain supplies an easy-to-use implementation of a markov chain text generator.  
To use it, you can simply do

    from pymarkovchain import MarkovChain
    # Create an instance of the markov chain, tell it where to load / save its database
    mc = MarkovChain("./markov")
    # generate the markov chain's language model
    mc.generateDatabase("This is a string of Text. It won't generate an interesting database though.")
    mc.generateString()

To store its data, PyMarkovChain simply uses pickle to dump all of its data to disk.
This entails that you have to use the same version of python to store the data and to
restore the data, as pickle is one of those things that have changed from python2 to python3.

See also [code on github](https://github.com/MaxWagner/PyMarkovChain) and [PyPI page](http://pypi.python.org/pypi/PyMarkovChain/).
To install, `pip install PyMarkovChain`
