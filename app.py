import re
import sys # for command line args
import time # for performance bechmarking
import pickle # To save markov_dict into a pickle file.
import cleanup # to cleanup source file
import tokenizer # turn source file into a list of tokens
import word_count # to get a histogram from source file
import sample # to generate a random sample of __ words from a source file
from markov_dictogram import MarkovDictogram # for custom markov chain
from flask import Flask, request, render_template # for webapp
app = Flask(__name__)
# ---dotenv setup---
# import os
# from dotenv import load_dotenv
# BASEDIR = os.path.abspath(os.path.dirname(__file__))
# load_dotenv(os.path.join(BASEDIR, '.env'))

# ---SAVE DATA INTO A PICKLE FILE---
def save_to_pickle(data, filename):
    '''data can be any type, name must be a string'''
    pickle.dump(data, open( filename, "wb" ))

def generate_dictogram(markov_order, pickle_url, corpus_url):
    corpus_content = cleanup.readFile(corpus_url)
    corpus_tokens = tokenizer.listOfTokens(corpus_content)
    start_time = time.time()
    potter_dictogram = MarkovDictogram(corpus_tokens, markov_order)
    run_time = time.time() - start_time
    print('time to create dictogram from: ' + corpus_url + 'was: ' + str(run_time))
    save_to_pickle(potter_dictogram, pickle_url)
    return potter_dictogram

def grab_dictogram(markov_order, pickle_url, corpus_url):
    try:
        start_time = time.time()
        dictogram = pickle.load(open(pickle_url, 'rb' ))
        run_time = time.time() - start_time
        print('successfully loaded dictogram file (' + pickle_url + ') in: ' + str(run_time))
    except:
        print('dictogram does not exist at url: ' + pickle_url)
        dictogram = generate_dictogram(markov_order, pickle_url, corpus_url)
    return dictogram

# LOAD UP MARKOV CHAIN FOR ALICE IN WONDERLAND
alice_markov_order = 2
alice_corpus_url = 'txt-files/alice.txt'
alice_pickle_url = 'alice_dictogram.p'
alice_dictogram = grab_dictogram(alice_markov_order, alice_pickle_url, alice_corpus_url)

# LOAD UP MARKOV CHAIN FOR H.POTTER AND METHODS OF RATIONALITY
potter_markov_order = 3
potter_corpus_url = 'txt-files/shorter-hpmor.txt'
potter_pickle_url = 'potter_dictogram.p'
potter_dictogram = grab_dictogram(potter_markov_order, potter_pickle_url, potter_corpus_url)

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
