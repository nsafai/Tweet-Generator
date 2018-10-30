import random # to generate random numbers
import re # for regular expressions

def histogramDict(url):
    file = open(url, 'r')

    content = file.read().lower()
    list_of_words = re.split('\W+', content) # replaces not (^) word characters with an empty string
    file.close()

    histogram = {} # create empty dictionary

    for word in list_of_words:
        if word in histogram:
            # increment counter at that key
            histogram[word] += 1
        else:
            # add to dictionary
            histogram[word] = 1

    return histogram # return a data structure that stores ea. unique word & of times the word appears

def histogramList(url):
    file = open(url, 'r')

    content = file.read().lower()
    list_of_words = re.split('\W+', content) # replaces not (^) word characters with an empty string
    file.close()

    unique_list_of_words = [] # create empty list
    counter = [] # empty list that will have count per word at same index as unique_list_of_words

    for word in list_of_words:
        if word in unique_list_of_words:
            counter[unique_list_of_words.index(word)] += 1 # increment counter for the same index
        else:
            # add to list
            unique_list_of_words.append(word)
            counter.append(1)

    histogram = []
    i = 0
    for word in unique_list_of_words:
        histogram.append([unique_list_of_words[i], counter[i]])
        i += 1

    return histogram # return a data structure that stores ea. unique word & of times the word appears

def histogramTuple(url):
    file = open(url, 'r')

    content = file.read().lower()
    list_of_words = re.split('\W+', content) # replaces not (^) word characters with an empty string
    file.close()

    unique_list_of_words = [] # create empty list
    counter = [] # empty list that will have count per word at same index as unique_list_of_words

    for word in list_of_words:
        if word in unique_list_of_words:
            counter[unique_list_of_words.index(word)] += 1 # increment counter for the same index
        else:
            # add to list
            unique_list_of_words.append(word)
            counter.append(1)

    histogram = []
    i = 0
    for word in unique_list_of_words:
        histogram.append((unique_list_of_words[i], counter[i]))
        i += 1

    return histogram # return a data structure that stores ea. unique word & of times the word appears

def unique_words(histogram):
    return len(histogram) # return the total count of unique words in the histogram.


def frequency(word, histogram):
    return histogram[word] # returns the number of times that word appea

if __name__ == '__main__':

    histogram = histogramDict('txt-files/edgarallanpoe.txt')
    print(histogram)

    # histogram = histogramList('txt-files/edgarallanpoe.txt')
    # print(histogram)
    #
    # histogram = histogramTuple('txt-files/edgarallanpoe.txt')
    # print(histogram)

    num_unique_words = unique_words(histogram) # get # of unique words from histogram dict
    print("There are " + str(num_unique_words) + " unique words in this file")

    frequency_of_the = frequency('the', histogram)
    print("The word THE appears " + str(frequency_of_the) + " times in this file")
