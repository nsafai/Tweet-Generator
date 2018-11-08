import sys # for command line args
import cleanup # to cleanup source file
import tokenizer # turn source file into a list of tokens
import word_count # to get a histogram from source file
import sample # to generate a random sample of __ words from a source file
# import sentence
from flask import Flask
app = Flask(__name__)

# --- FUNCTIONS BASED ON MODULES IMPORTED ABOVE ---
def sampleWords(source_text, num_words):
    sample_words = sample.generateRandomSentence(dict_of_probability, num_words)
    return sample_words

# --- ROUTES ---
@app.route('/')
def index():
    num_words = 23
    sample_words = sampleWords(source_text, num_words)
    return sample_words

@app.route('/<num_words>')
def generate_sentence(num_words):
    sample_words = sampleWords(source_text, int(num_words))
    return sample_words

if __name__ == '__main__':
    # code to run when file is executed
    app.debug = True
    app.run(host='0.0.0.0' , port=5000)

    source_text = 'txt-files/edgarallanpoe.txt'
    content = cleanup.readFile(source_text)
    list_of_tokens = tokenizer.listOfTokens(content)
    histogram_dict = word_count.histogramDict(list_of_tokens)
    dict_of_probability = sample.dictionaryOfProbability(histogram_dict)
    # -- TO DEBUG BY RUNNING SCRIPT, UNCOMMENT BELOW --
    # num_words = 23
    # sample_words = sampleWords('txt-files/edgarallanpoe.txt', num_words)
    # print(sample_words)
