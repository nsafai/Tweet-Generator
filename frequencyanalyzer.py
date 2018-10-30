import random # to generate random numbers
import re # for regular expressions

def histogramDict(url):
    f = open(url, 'r')

    content = f.read().lower()
    list_of_words = re.split('\W+', content) # replaces not (^) word characters with an empty string
    f.close()

    histogram = {} # create empty dictionary

    for word in list_of_words:
        if word in histogram:
            # increment counter at that key
            histogram[word] += 1
        else:
            # add to dictionary
            histogram[word] = 1

    # return a histogram data structure that stores each unique word
    # along with the number of times the word appears in the source text.
    return histogram

def histogramList(url):
    f = open(url, 'r')

    content = f.read().lower()
    list_of_words = re.split('\W+', content) # replaces not (^) word characters with an empty string
    f.close()

    unique_list_of_words = [] # create empty list
    counter = []

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

    # return a histogram data structure that stores each unique word
    # along with the number of times the word appears in the source text.
    return histogram

def histogramTuple(url):
    f = open(url, 'r')

    content = f.read().lower()
    list_of_words = re.split('\W+', content) # replaces not (^) word characters with an empty string
    f.close()

    unique_list_of_words = [] # create empty list
    counter = []

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

    # return a histogram data structure that stores each unique word
    # along with the number of times the word appears in the source text.
    return histogram

def unique_words(histogram):
    unique_words = []

    for key in histogram:
        if histogram[key] == 1: # if word counter is 1
            unique_words.append(histogram[key]) # add to unique_words list

    return len(unique_words)
    # return the total count of unique words in the histogram.

def frequency(word, histogram):
    return histogram[word]
    # returns the number of times that word appears in a text.
    # For example, when given the word "mystery" and the Holmes histogram, it will return the integer 20.

if __name__ == '__main__':

    histogram = histogramDict('txt-files/edgarallanpoe.txt')
    print(histogram)

    # histogram = histogramList('txt-files/blogpost.txt')
    # print(histogram)
    #
    # histogram = histogramTuple('txt-files/blogpost.txt')
    # print(histogram)

    num_unique_words = unique_words(histogram) # get # of unique words from histogram dict
    print("There are " + str(num_unique_words) + " unique words in this file")

    frequency_of_the = frequency('the', histogram)
    print("The word THE appears " + str(frequency_of_the) + " times in this file")

    # print "sets      :",timeit.Timer('f(s)', 'from __main__ import s,test_set as f').timeit(1000000)
    # print "regex     :",timeit.Timer('f(s)', 'from __main__ import s,test_re as f').timeit(1000000)
