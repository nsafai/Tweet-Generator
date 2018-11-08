# module for generating a sample word from a histogram
import sys # for command line args
import cleanup # to cleanup source file
import tokenize # turn source file into a list of tokens
import word_count # to get a histogram from source file
import random

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
    params = sys.argv[1:] # take a list of arguments, starting from index 1 till the end
    source_text = str(params[0]) # url for source_text
    num_words = int(params[1]) # number of sample words to generate

    content = cleanup.readFile(source_text)
    list_of_tokens = tokenize.listOfTokens(content)
    histogram = word_count.histogramDict(list_of_tokens)
    dictionaryOfProbability = dictionaryOfProbability(histogram)
    sentence, test_dict = generateRandomSentence(dictionaryOfProbability, num_words)
    print(sentence)
