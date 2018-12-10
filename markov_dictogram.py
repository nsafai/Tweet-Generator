#!python

from dictogram import Dictogram

class MarkovDictogram(Dictogram):
    """Takes a list of words and generates a dictionary of dictograms of each word directly following each word"""

    def __init__(self, word_list=None, markov_order=2):
        """Initialize this histogram as a new dict and count given words."""
        super(MarkovDictogram, self).__init__()  # Initialize this as a Dictogram
        self.word_list = word_list
        self.markov_order = markov_order

        if word_list is not None: #safety check
            word_list_length = len(word_list) - (markov_order*2) # ea. word except a markov_order window * 2

            for word_index in range(word_list_length):
                first_words = []
                next_words = []

                for n in range(markov_order):
                    first_words.append(word_list[word_index + n])
                    next_words.append(word_list[word_index + (markov_order-1) + n])

                first_words_tuple = tuple(first_words)
                next_words_tuple = tuple(next_words)

                self.add_count(first_words_tuple, next_words_tuple)

    def add_count(self, first_words, next_words):

        """Counts how many times next_word follows word"""
        if first_words in self: # word is already in MarkovDictogram
            if next_words in self[first_words]: # alrdy seen next_word after word
                self[first_words][next_words] += 1 # word dictogram at index = [next_word]
            else:
                self[first_words][next_words] = 1 # 1st time seeing next_word after word
        else: # never seen word before
            self[first_words] = {next_words:1}

    def frequency(self, first_words, next_words):
        """Return # times next_word follows word, or 0 if never."""
        if next_words in self[first_words]:
            return self[first_words][next_words]
        else:
            return 0

if __name__ == '__main__':
    import sys

    # Test markov dictogram
    seuss_text = """So be sure when you step, step with care and great tact.
    And remember that life’s A Great Balancing Act. And will you succeed? Yes!
    You will, indeed! 98 and ¾ percent guaranteed. Kid, you’ll move mountains."""

    markov_histogram = MarkovDictogram(fish_text.split())
    print('MarkovDictogram: {}'.format(markov_histogram))
