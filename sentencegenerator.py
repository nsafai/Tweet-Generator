import sys # to access command line arguments
import random # to generate random numbers
import re # for regular expressions

def readFile(url):
    f = open(url, 'r') # open file at URL
    content = f.read() # split file up lines and add each linne to an array named 'content'
    f.close()
    list_of_words = re.split('\W+', content)
    return list_of_words

def returnRandomWords(content, num_words):
    sentence = []
    count = 0
    while count < num_words:
        random_word = random.choice(content)
        sentence.append(random_word)
        count+= 1
    return (' '.join(sentence).lower())


if __name__ == '__main__':
    # params = sys.argv[1:] # take a list of arguments, starting from index 1 till the end
    # num_words = 20 # num_words stores the number of words to use when generating a sentence
    content = readFile('txt-files/edgarallanpoe.txt')
    random_words = returnRandomWords(content, num_words)
    print(random_words)
