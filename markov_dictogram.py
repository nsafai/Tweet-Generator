#!python

from dictogram import Dictogram

class MarkovDictogram(Dictogram):
    """Takes a list of words and generates a dictionary of dictograms of each word directly following each word"""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new dict and count given words."""
        super(MarkovDictogram, self).__init__()  # Initialize this as a Dictogram

        if word_list is not None: #safety check
            word_list_length = len(word_list)
            for word_index in range(word_list_length - 1): # ea. word except last (because no following word)
                self.add_count(word_list[word_index],word_list[word_index+1])
                print(self)


    def add_count(self, word, next_word):
        """Counts how many times next_word follows word"""
        if word in self: # word is in MarkovDictogram
            if next_word in self[word]: # alrdy seen next_word after word
                self[word][next_word] += 1
            else:
                self[word][next_word] = 1 # 1st time seeing next_word after word
        else: # never seen word before
            self[word] = {next_word:1}

    def frequency(self, word, next_word):
        """Return # times next_word follows word, or 0 if never."""
        if next_word in self[word]:
            return self[word][next_word]
        else:
            return 0

if __name__ == '__main__':
    import sys
    # arguments = sys.argv[1:]  # Exclude script name in first argument

    # Test histogram on words in a classic book title
    fish_text = 'one fish two fish red fish blue fish'
    markov_histogram = MarkovDictogram(fish_text.split())
    print('MarkovDictogram: {}'.format(markov_histogram))
