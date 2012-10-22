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
