import cleanup
import tokenize
import word_count
import sample
import sentence
from flask import Flask
app = Flask(__name__)

# define some functions that compose the above modules
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
    app.debug = True
    app.run(host='0.0.0.0' , port=5000)
