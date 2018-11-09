# module for generating a sample word from a histogram
import sys # for command line args
import cleanup # to cleanup source file
import tokenizer # turn source file into a list of tokens
import word_count # to get a histogram from source file
import random
import time


def generateWord(histogram_dict):
    total_number_tokens = sum(histogram_dict.values())
    random_chance = random.randint(1, total_number_tokens)
    running_total = 1
    # items() turns a dictionary into an iterable obj
    for key, value in histogram_dict.items():
        running_total += value
        if running_total > random_chance:

            return key
        else:
            continue


def generateSentence(histogram, num_words):
    start_time = time.time()
    counter = 0
    sentence = []
    while counter < num_words:
        sentence.append(generateWord(histogram))
        counter += 1
    run_time = time.time() - start_time
    print('run time: ' + str(run_time))
    clean_sentence = ' '.join(sentence).capitalize() + str(".")
    return clean_sentence

def sentenceTester(sentence):
    test_dict = {}
    for word in sentence:
        if word not in test_dict:
            # add to dict
            test_dict[word] = 1
        else:
            # already exists in dict so increment counter at that key
            test_dict[word] += 1
    return test_dict


if __name__ == '__main__':
    params = sys.argv[1:] # take a list of arguments, starting from index 1 till the end
    source_text = str(params[0]) # url for source_text
    num_words = int(params[1]) # number of sample words to generate
    content = cleanup.readFile(source_text)
    list_of_tokens = tokenizer.listOfTokens(content)
    histogram = word_count.histogramDict(list_of_tokens)
    sentence = generateSentence(histogram, num_words)
    test_dict = sentenceTester(sentence)
    print(sentence)
    print(test_dict)
