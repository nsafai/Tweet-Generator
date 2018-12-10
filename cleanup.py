# module for cleaning up source text and turning text into a list of tokens
import random # to generate random numbers
import re # for regular expressions
import sys # for command line args

def readFile(url):
    file = open(url, 'r')
    content = file.read()
    content_wo_contractions = decontracted(content)
    # content_wo_symbols = re.sub(r'[^\w]', ' ', content_wo_contractions);
    content_wo_mult_spaces = re.sub(r"\s+"," ", content_wo_contractions, flags = re.I)
    # clean_content_lower = content_wo_mult_spaces.lower()
    clean_content = re.sub(r" i ", " I ", content_wo_mult_spaces)
    file.close()
    return clean_content

def decontracted(phrase):
    # taken from https://stackoverflow.com/a/47091490/3247102
    # specific
    phrase = re.sub(r"won’t", "will not", phrase)
    phrase = re.sub(r"can\’t", "can not", phrase)

    # general
    phrase = re.sub(r"n\’t", " not", phrase)
    phrase = re.sub(r"\’re", " are", phrase)
    # phrase = re.sub(r"\’s", " is", phrase) # commented about because breaks on possessive (ex: someone's)
    phrase = re.sub(r"\’d", " would", phrase)
    phrase = re.sub(r"\’ll", " will", phrase)
    phrase = re.sub(r"\’t", " not", phrase)
    phrase = re.sub(r"\’ve", " have", phrase)
    phrase = re.sub(r"\’m", " am", phrase)
    # print(phrase)
    return phrase

if __name__ == '__main__':
    params = sys.argv[1:] # take a list of arguments, starting from index 1 till the end
    source_text = str(params[0]) # url for source_text
    content = readFile(source_text)
    print(content)
