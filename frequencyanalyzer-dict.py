import random # to generate random numbers
import re # for regular expressions

def histogramDict(url):
    file = open(url, 'r')
    content = file.read().lower()
    list_of_words = re.split('\W+', content) # replaces not (^) word characters with an empty string
    file.close()
    histogram = {} # create empty dictionary
    for word in list_of_words:
        if word not in histogram:
            # add to dictionary
            histogram[word] = 1
        else:
            # already exists in dictionary, so increment counter at that key
            histogram[word] += 1
    return histogram # return a data structure that stores ea. unique word & of times the word appears

def unique_words(histogram):
    return len(histogram) # return the total count of unique words in the histogram.

def frequency(word, histogram):
    return histogram[word] # returns the number of times that word appea

if __name__ == '__main__':

    histogram = histogramDict('txt-files/edgarallanpoe.txt')
    print(histogram)
    num_unique_words = unique_words(histogram) # get # of unique words from histogram dict
    print("There are " + str(num_unique_words) + " unique words in this file")
    frequency_of_the = frequency('the', histogram)
    print("The word THE appears " + str(frequency_of_the) + " times in this file")
