import random # to generate random numbers
import re # for regular expressions
import sys # for command line args

def readFile(url):
    file = open(url, 'r')
    content = file.read().lower()
    file.close()
    return content

def listOfWords(content):
    list_of_words = re.split('\W+', content) # replaces not (^) word characters with an empty string
    list_of_words.pop() # trim any empty words (last word of list seems to always be empty)
    return list_of_words

if __name__ == '__main__':
    params = sys.argv[1:] # take a list of arguments, starting from index 1 till the end
    source_text = str(params[0]) # url for source_text
    content = readFile(source_text)
    list_of_words = listOfWords(content)
    print(list_of_words)
