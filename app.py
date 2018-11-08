from flask import Flask
app = Flask(__name__)
import stochasticsampling

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
    num_words = 20
    content = stochasticsampling.readFile('txt-files/edgarallanpoe.txt')
    histogram = stochasticsampling.histogramDict(content)
    dictionaryOfProbability = stochasticsampling.dictionaryOfProbability(histogram)
    sentence, test_dict = stochasticsampling.generateRandomSentence(dictionaryOfProbability, num_words)

    return str(sentence)

@app.route('/<number>')
def generate_sentence(num_words):
    # show the user profile for that user
    content = stochasticsampling.readFile('txt-files/edgarallanpoe.txt')
    histogram = stochasticsampling.histogramDict(content)
    dictionaryOfProbability = stochasticsampling.dictionaryOfProbability(histogram)
    sentence, test_dict = stochasticsampling.generateRandomSentence(dictionaryOfProbability, int(num_words))

    return str(sentence)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0' , port=5000)
