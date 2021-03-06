import random # to generate random numbers
import re # for regular expressions

def histogramTuple(url):
    file = open(url, 'r')
    content = file.read().lower()
    list_of_tokens = re.split('\W+', content) # replaces not (^) word characters with an empty string
    file.close()
    unique_list_of_tokens = [] # create empty list
    word_counter = [] # empty list that will have count per word at same index as unique_list_of_tokens
    for word in list_of_tokens:
        if word not in unique_list_of_tokens:
            # add to list
            unique_list_of_tokens.append(word)
            word_counter.append(1)
        else:
            # word is already in list, increment word_counter at same index as word
            word_counter[unique_list_of_tokens.index(word)] += 1 # increment word_counter for the same index
    histogram = []
    i = 0
    for word in unique_list_of_tokens:
        histogram.append((unique_list_of_tokens[i], word_counter[i]))
        i += 1
    return histogram # return a data structure that stores ea. unique word & of times the word appears

def unique_words(histogram):
    return len(histogram) # return the total count of unique words in the histogram.


def frequency(word, histogram):
    return histogram[word] # returns the number of times that word appea

if __name__ == '__main__':
    histogram = histogramTuple('txt-files/edgarallanpoe.txt')
    print(histogram)
    num_unique_words = unique_words(histogram) # get # of unique words from histogram dict
    print("There are " + str(num_unique_words) + " unique words in this file")
    frequency_of_the = frequency('the', histogram)
    print("The word THE appears " + str(frequency_of_the) + " times in this file")
