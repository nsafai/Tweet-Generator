import sys # for command line args
import cleanup # to cleanup source file
import tokenizer # turn source file into a list of tokens
import word_count # to get a histogram from source file
import sample # to generate a random sample of __ words from a source file
from markov_dictogram import MarkovDictogram
from flask import Flask, request, render_template
app = Flask(__name__)

# OPEN UP SOURCE FILE ONCE ONLY
markov_order = 4
source_text = 'txt-files/alice.txt'
content = cleanup.readFile(source_text)
list_of_tokens = tokenizer.listOfTokens(content)
word_histogram = word_count.histogramDict(list_of_tokens)
markov_dictogram = MarkovDictogram(list_of_tokens, markov_order)

# --- ROUTES ---
@app.route('/')
def index():
    num_words = request.args.get('num', default=60, type=int)
    # markov_sentence = sample.generateMarkovSentence(word_histogram, markov_dictogram, num_words)
    markov_sentence = sample.generateNthOrderMarkovSentence(markov_dictogram, num_words, markov_order)
    return render_template('home.html', markov_sentence=markov_sentence)

if __name__ == '__main__':
    # code to run when file is executed 'flask run'
    app.debug = True
    app.run(host='0.0.0.0' , port=5000)
    # -- TO DEBUG BY RUNNING SCRIPT, UNCOMMENT BELOW --
    # num_words = 500
    # sentence = sample.generateSentence(histogram, num_words)
    # print(sentence)
