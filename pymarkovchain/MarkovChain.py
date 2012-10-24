import pickle
import sys
import random


class MarkovChain(object):
    def __init__(self, dbFilePath="markovdb"):
        self.dbFilePath = dbFilePath
        try:
            with open(dbFilePath, 'rb') as dbfile:
                self.db = pickle.load(dbfile)
        except IOError as e:
            sys.stderr.write('Database file not found, using empty database\n')
            self.db = {}

    def generateDatabase(self, textSample):
        """ Generate word probability database from raw content string """
        # I'm using the database to temporarily store word counts
        textSample = textSample.split('\n')  # split lines
        # We're using "" as special symbol standing for the beginning
        # of a sentence
        self.db = {"": {"": 0.0}}
        for line in textSample:
            words = line.split()  # split words in line
            if len(words) == 0:
                continue
            # first word follows a sentence end
            if words[0] in self.db[""]:
                self.db[""][words[0]] += 1
            else:
                self.db[""][words[0]] = 1.0
            for i in range(len(words) - 1):
                if words[i] in self.db:
                    # the current word has been found at least once
                    # increment parametrized wordcounts
                    if words[i + 1] in self.db[words[i]]:
                        self.db[words[i]][words[i + 1]] += 1
                    else:
                        self.db[words[i]][words[i + 1]] = 1.0
                else:
                    # word has been found for the first time
                    self.db[words[i]] = {words[i + 1]: 1.0}
            # last word precedes a sentence end
            if words[len(words) - 1] in self.db:
                if "" in self.db[words[len(words) - 1]]:
                    self.db[words[len(words) - 1]][""] += 1
                else:
                    self.db[words[len(words) - 1]][""] = 1.0
            else:
                self.db[words[len(words) - 1]] = {"": 1.0}

        # We've now got the db filled with parametrized word counts
        # We still need to normalize this to represent probabilities
        for word in self.db:
            wordsum = 0
            for nextword in self.db[word]:
                wordsum += self.db[word][nextword]
            if wordsum != 0:
                for nextword in self.db[word]:
                    self.db[word][nextword] /= wordsum
        # Now we dump the db to disk
        try:
            with open(self.dbFilePath, 'wb') as dbfile:
                pickle.dump(self.db, dbfile)
            # It looks like db was written successfully
            return True
        except IOError as e:
            sys.stderr.write('Database file could not be written')
            return False

    def generateString(self):
        """ Generate a "sentence" with the database of known text """
        return self._accumulateWithSeed("", "")

    def generateStringWithSeed(self, seed):
        """ Generate a "sentence" with the database and a given word """
        if seed in self.db:
            return self._accumulateWithSeed("", seed)
        # Just pretend we've managed to generate a sentence.
        sep = " "
        if seed == "":
            sep = ""
        return seed + sep + self.generateString()

    def _accumulateWithSeed(self, sentence, lastWord):
        """ Accumulate the generated sentence """
        nextWord = self._nextWord(lastWord)
        if sentence == "":
            sep = ""
        else:
            sep = " "
        if nextWord == "":
            return sentence + sep + lastWord
        return self._accumulateWithSeed(sentence + sep + lastWord, nextWord)

    def _nextWord(self, lastword):
        probmap = self.db[lastword]
        sample = random.random()
        # since rounding errors might make us miss out on some words
        maxprob = 0.0
        maxprobword = ""
        for candidate in probmap:
            # remember which word had the highest probability
            # this is the word we'll default to if we can't find anythin else
            if probmap[candidate] > maxprob:
                maxprob = probmap[candidate]
                maxprobword = candidate
            if sample > probmap[candidate]:
                sample -= probmap[candidate]
            else:
                return candidate
        # getting here means we haven't found a matching word. :(
        return maxprobword
