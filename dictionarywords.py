import sys # to access command line arguments
import random # to generate random numbers

def readFile(url):
    f = open(url, 'r') # open file at URL
    content = f.read().splitlines() # split file up lines and add each linne to an array named 'content'
    f.close()
    return content

def returnRandomWords(content, num_words):
    sentence = []
    count = 0
    while count < num_words:
        random_word = random.choice(content)
        sentence.append(random_word)
        count+= 1
    return sentence


if __name__ == '__main__':
    params = sys.argv[1:] # take a list of arguments, starting from index 1 till the end
    num_words = int(params[0]) # num_words stores the number of words to use when generating a sentence
    # content = readFile('/usr/share/dict/words') # read /usr/share/dict/words
    content = readFile('txt-files/edgarallanpoe.txt')

    random_words = returnRandomWords(content, num_words)
    # print(*random_words) # using a * removes the ugly "[" syntax from the console output
