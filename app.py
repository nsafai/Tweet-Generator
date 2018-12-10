import re
import sys # for command line args
import cleanup # to cleanup source file
import tokenizer # turn source file into a list of tokens
import word_count # to get a histogram from source file
import sample # to generate a random sample of __ words from a source file
from markov_dictogram import MarkovDictogram
from flask import Flask, request, render_template
app = Flask(__name__)

# ---dotenv setup---
import os
from dotenv import load_dotenv
BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))

# ---genius API setup---
import lyricsgenius as genius
genius_client_token = os.getenv("GENIUS_CLIENT_ACCESS_TOKEN")
api = genius.Genius(genius_client_token)


# ---IMPORT ALICE IN WONDERLAND---
alice_markov_order = 2
alice_corpus_url = 'txt-files/alice.txt'
alice_content = cleanup.readFile(alice_corpus_url)
alice_tokens = tokenizer.listOfTokens(alice_content)
alice_dictogram = MarkovDictogram(alice_tokens, alice_markov_order)

# -- IMPORT BEATLES LYRICS --
beatles_markov_order = 3
beatles_corpus_url = 'beatles_lyrics.json'
beatles_content = cleanup.readAndCleanGeniusLyrics(beatles_corpus_url)
beatles_tokens = tokenizer.listOfTokens(beatles_content)
beatles_dictogram =  MarkovDictogram(beatles_tokens, beatles_markov_order)



# ---ROUTES---
@app.route('/')
def index():
    num_words = request.args.get('num', default=40, type=int)
    theme = request.args.get('theme', default='alice')
    if theme == 'beatles':
        markov_sentence = sample.generateNthOrderMarkovSentence(beatles_markov_order, num_words, beatles_markov_order)
    else:
        markov_sentence = sample.generateNthOrderMarkovSentence(alice_dictogram, num_words, alice_markov_order)

    return render_template('home.html', markov_sentence=markov_sentence)


# ---RUN CODE---
if __name__ == '__main__':
    # code to run when file is executed 'flask run'
    app.debug = True
    app.run(host='0.0.0.0' , port=5000)
    # -- TO DEBUG BY RUNNING SCRIPT, UNCOMMENT BELOW --
    # num_words = 500
    # sentence = sample.generateSentence(histogram, num_words)
    # print(sentence)
