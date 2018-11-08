from flask import Flask
app = Flask(__name__)
import stochasticsampling
import dictionarywords

# @app.route('/')
# def index():
#     content = stochasticsampling.readFile('txt-files/fish.txt')
#     # app.logger.debug(content)
#     histogram = stochasticsampling.histogramDict(content)
#     # app.logger.debug(histogram)
#     dictionaryOfProbability = stochasticsampling.dictionaryOfProbability(histogram)
#     # app.logger.debug(dictionaryOfProbability)
#     result = stochasticsampling.generateRandomSentence(dictionaryOfProbability, 100)
#     # app.logger.debug(result)
#     return str(result)

@app.route('/')
def index():
    num_words = 10 # num_words stores the number of words to use when generating a sentence
    content = dictionarywords.readFile('/usr/share/dict/words') # read /usr/share/dict/words

    random_words = dictionarywords.returnRandomWords(content, num_words)
    return str(', '.join(random_words))
