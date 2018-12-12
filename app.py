import re
import sys # for command line args
import cleanup # to cleanup source file
import tokenizer # turn source file into a list of tokens
import word_count # to get a histogram from source file
import sample # to generate a random sample of __ words from a source file
from markov_dictogram import MarkovDictogram
from flask import Flask, request, render_template
import time
app = Flask(__name__)
# ---dotenv setup---
# import os
# from dotenv import load_dotenv
# BASEDIR = os.path.abspath(os.path.dirname(__file__))
# load_dotenv(os.path.join(BASEDIR, '.env'))


# ---IMPORT ALICE IN WONDERLAND---
def generate_alice_dictogram(alice_markov_order=2):

    alice_corpus_url = 'txt-files/alice.txt'
    alice_content = cleanup.readFile(alice_corpus_url)
    alice_tokens = tokenizer.listOfTokens(alice_content)
    start_time = time.time()
    alice_dictogram = MarkovDictogram(alice_tokens, alice_markov_order)
    run_time = time.time() - start_time
    print('time to dictogram alice: ' + str(run_time))
    return alice_dictogram
# print(alice_dictogram)

# ---IMPORT HPOTTER MOR---
def generate_potter_dictogram(potter_markov_order=2):

    potter_corpus_url = 'txt-files/shorter-hpmor.txt'
    potter_content = cleanup.readFile(potter_corpus_url)
    potter_tokens = tokenizer.listOfTokens(potter_content)
    start_time = time.time()
    potter_dictogram = MarkovDictogram(potter_tokens, potter_markov_order)
    run_time = time.time() - start_time
    print('time to dictogram potter: ' + str(run_time))
    return potter_dictogram

alice_markov_order = 2
alice_dictogram = generate_alice_dictogram(alice_markov_order)
potter_markov_order = 3
potter_dictogram = generate_potter_dictogram(potter_markov_order)

# ---ROUTES---
@app.route('/')
@app.route('/alice')
def index():
    num_words = request.args.get('num', default=40, type=int)
    markov_sentence = sample.generateNthOrderMarkovSentence(alice_dictogram, num_words, alice_markov_order)

    return render_template('home.html', markov_sentence=markov_sentence, default='alice')

@app.route('/potter')
def show_potter_quote():
    num_words = request.args.get('num', default=40, type=int)
    markov_sentence = sample.generateNthOrderMarkovSentence(potter_dictogram, num_words, potter_markov_order)

    return render_template('home.html', markov_sentence=markov_sentence, default='potter')

# ---RUN CODE---
if __name__ == '__main__':
    # code to run when file is executed 'flask run'
    app.debug = True
    app.run(host='0.0.0.0' , port=5000)
    # -- TO DEBUG BY RUNNING SCRIPT, UNCOMMENT BELOW --
    # num_words = 500
    # sentence = sample.generateSentence(histogram, num_words)
    # print(sentence)
