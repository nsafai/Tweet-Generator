import sys # for command line args
import cleanup # to cleanup source file
import tokenize # turn source file into a list of tokens
import word_count # to get a histogram from source file
import sample # to generate a random sample of __ words from a source file
# import sentence
# from flask import Flask
# app = Flask(__name__)

# define some functions that compose the above modules
def readFile(source_text):
    return cleanup.readFile(source_text)

def listOfTokens(content):
    return tokenize.listOfTokens(content)

def histogram(tokens):
    return word_count.histogramDict(tokens)

def dictionaryOfProbability(histogram):
    return sample.dictionaryOfProbability(histogram)

def generateRandomSentence(dictionaryOfProbability, num_words):
    return sample.generateRandomSentence(dictionaryOfProbability, num_words)

# @app.route('/')
# def index():
#     num_words = 20
#     content = stochasticsampling.readFile('txt-files/edgarallanpoe.txt')
#     histogram = stochasticsampling.histogramDict(content)
#     dictionaryOfProbability = stochasticsampling.dictionaryOfProbability(histogram)
#     sentence, test_dict = stochasticsampling.generateRandomSentence(dictionaryOfProbability, num_words)
#
#     return str(sentence)
#
# @app.route('/<num_words>')
# def generate_sentence(num_words):
#     # show the user profile for that user
#     content = stochasticsampling.readFile('txt-files/edgarallanpoe.txt')
#     histogram = stochasticsampling.histogramDict(content)
#     dictionaryOfProbability = stochasticsampling.dictionaryOfProbability(histogram)
#     sentence, test_dict = stochasticsampling.generateRandomSentence(dictionaryOfProbability, int(num_words))
#
#     return str(sentence)

if __name__ == '__main__':
    # code to run when file is executed
    # app.debug = True
    # app.run(host='0.0.0.0' , port=5000)

    params = sys.argv[1:] # take a list of arguments, starting from index 1 till the end
    source_text = str(params[0]) # url for source_text
    num_words = int(params[1]) # number of sample words to generate

    content = readFile(source_text)
    list_of_tokens = listOfTokens(content)
    histogram = histogram(list_of_tokens)
    dictionaryOfProbability = dictionaryOfProbability(histogram)
    sentence, test_dict = generateRandomSentence(dictionaryOfProbability, num_words)
    print(sentence)
