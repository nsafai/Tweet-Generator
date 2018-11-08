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
    counter = 1
    test_dict = {}
    list_of_word_types = list(dictionaryOfProbability.keys())
    sentence = []
    while counter < num_words:
        random_word = random.choice(list_of_word_types)
        random_chance = random.random()
        if dictionaryOfProbability[random_word] > random_chance:
            sentence.append(random_word)
            if random_word not in test_dict: # counter function
                # add to dictionary
                test_dict[random_word] = 1
            else:
                # already exists in dictionary, so increment counter at that key
                test_dict[random_word] += 1
            counter += 1
    return (' '.join(sentence)), test_dict


if __name__ == '__main__':
    num_words = 100
    content = readFile('txt-files/edgarallanpoe.txt')
    histogram = histogramDict(content)
    dictionaryOfProbability = dictionaryOfProbability(histogram)
    sentence, test_dict = generateRandomSentence(dictionaryOfProbability, num_words)
    print(sentence)
