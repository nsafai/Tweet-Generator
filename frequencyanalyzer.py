import sys # to access command line arguments
import random # to generate random numbers

def histogram(url):
    f = open(url, 'r')
    content = f.read().split()
    f.close()

    histogram = {} # create empty dictionary

    for word in content:
        if word in histogram:
            # increment counter at that key
            histogram[word] += 1
        else:
            # add to dictionary
            histogram[word] = 1

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

    # read /usr/share/dict/words
    histogram = histogram('txt-files/blogpost.txt')
    print(histogram)

    num_unique_words = unique_words(histogram) # get # of unique words from histogram dict
    print("There are " + str(num_unique_words) + " unique words in this file")

    frequency_of_the = frequency('the', histogram)
    print("The word THE appears " + str(frequency_of_the) + " times in this file")
