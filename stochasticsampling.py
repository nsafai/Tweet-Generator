import random # to generate random numbers
import re # for regular expressions

def readFile(url):
    file = open(url, 'r')
    content = file.read().lower()
    file.close()
    return content

def histogramDict(content):
    list_of_words = re.split('\W+', content) # replaces not (^) word characters with an empty string
    histogram = {} # create empty dictionary
    for word in list_of_words:
        if word not in histogram:
            # add to dictionary
            histogram[word] = 1
        else:
            # already exists in dictionary, so increment counter at that key
            histogram[word] += 1
    histogram.pop('') # for some reason the reg expression above adds a key '' that needs to be removed
    return histogram # return a data structure that stores ea. unique word & of times the word appears


def unique_words(histogram):
    return len(histogram) # return the total count of unique words in the histogram.


def frequency(word, histogram):
    return histogram[word] # returns the number of times that word appea


def dictionaryOfProbability(histogram):
    total_number_words = sum(histogram.values())
    dictionaryOfProbability = {}
    for word in histogram:
        dictionaryOfProbability[word] = frequency(word, histogram) / total_number_words
    return dictionaryOfProbability

def generateRandomSentence(dictionaryOfProbability, num_words):
    counter = 0
    list_of_word_types = list(dictionaryOfProbability.keys())
    while counter < num_words:
        random_word = random.choice(list_of_word_types)
        random_chance = random.random()
        lower_bound = random_chance * 0.9
        upper_bound = random_chance * 1.1

        if dictionaryOfProbability[random_word] > random_chance:
            print(random_word)
            counter += 1

        # grab a random word from dictionary based on probability key in dictionaryOfProbability


if __name__ == '__main__':
    content = readFile('txt-files/fish.txt')
    histogram = histogramDict(content)
    dictionaryOfProbability = dictionaryOfProbability(histogram)
    generateRandomSentence(dictionaryOfProbability, 16)