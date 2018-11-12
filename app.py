import sys # for command line args
import cleanup # to cleanup source file
import tokenizer # turn source file into a list of tokens
import word_count # to get a histogram from source file
import sample # to generate a random sample of __ words from a source file
from markov_dictogram import MarkovDictogram
from flask import Flask, request
app = Flask(__name__)

# OPEN UP SOURCE FILE ONCE ONLY
source_text = 'txt-files/alice.txt'
content = cleanup.readFile(source_text)
list_of_tokens = tokenizer.listOfTokens(content)
word_histogram = word_count.histogramDict(list_of_tokens)
markov_dictogram = MarkovDictogram(list_of_tokens)


# --- ROUTES ---
@app.route('/')
def index():
    num_words = request.args.get('num', default=23, type=int)
    markov_sentence = sample.generateMarkovSentence(word_histogram, markov_dictogram, num_words)
    return markov_sentence

# @app.route('/<num_words>')
# def generate_sentence(num_words):
#     sentence = sample.generateSentence(histogram, num_words)
#     return sentence

if __name__ == '__main__':
    # code to run when file is executed
    app.debug = True
    app.run(host='0.0.0.0' , port=5000)
    # -- TO DEBUG BY RUNNING SCRIPT, UNCOMMENT BELOW --
    # num_words = 500
    # sentence = sample.generateSentence(histogram, num_words)
    # print(sentence)
