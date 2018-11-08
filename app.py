from flask import Flask
app = Flask(__name__)
import sentencegenerator

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
    num_words = 20 # num_words stores the number of words to use when generating a sentence
    content = sentencegenerator.readFile('txt-files/edgarallanpoe.txt')
    random_words = sentencegenerator.returnRandomWords(content, num_words)

    return str(random_words)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0' , port=5000)
