# module for turning clean source text into a list of tokens
import random # to generate random numbers
import re # for regular expressions
import sys # for command line args
import cleanup # clean up source text

def listOfTokens(content):
    list_of_tokens = re.split('\W+', content) # replaces not (^) word characters with an empty string
    list_of_tokens.pop() # trim any empty words (last word of list seems to always be empty)
    return list_of_tokens

if __name__ == '__main__':
    params = sys.argv[1:] # take a list of arguments, starting from index 1 till the end
    source_text = str(params[0]) # url for source_text

    content = cleanup.readFile(source_text)
    list_of_tokens = listOfTokens(content)
    print(list_of_tokens)
