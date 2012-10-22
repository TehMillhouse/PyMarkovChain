import pickle
import sys


class MarkovChain(object):
    def __init__(self, dbFilePath="markovdb"):
        self.dbFilePath = dbFilePath
        try:
            with open(dbFilePath) as dbfile:
                self.db = pickle.load(dbfile)
        except IOError as e:
            sys.stderr.write('Database file not found, using empty database\n')
            self.db = {}

    def generateDatabase(self, textSample):
        """ Generate word probability database from raw content string """
        # I'm using the database to temporarily store word counts
        textSample = textSample.split('\n')  # split lines
        for line in textSample:
            words = line.split()  # split words in line
            for i in range(len(words)):
                if words[i] in self.db:
                    pass
                    # the current word has been found at least once
                    # increment parametrized wordcounts
                    # TODO
                else:
                    pass
                    # word has been found for the first time
                    # TODO
        # We've now got the db filled with parametrized word counts
        # We still need to normalize this to represent probabilities
        # TODO
        self.db = {}

        try:
            with open(self.dbFilePath, 'wb') as dbfile:
                pickle.dump(self.db, dbfile)
                # It looks like db was written successfully
                return True
        except IOError as e:
            sys.stderr.write('Database file could not be written')
            return False

    def generateString(self):
        # TODO implement actual markov chain
        return "This is just a placeholder"
