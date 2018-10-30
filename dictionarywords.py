import sys # to access command line arguments
import random # to generate random numbers

def readFile(url):
    f = open(url, 'r')
    content = f.read().splitlines()
    f.close()
    # print(content)
    return content

if __name__ == '__main__':
    params = sys.argv[1:] # take a list of arguments, starting from index 1 till the end
    num_words = int(params[0]) # num_words stores the number of words to use when generating a sentence

    # read /usr/share/dict/words
    content = readFile('/usr/share/dict/words')
    sentence = []
    count = 0
    while count < num_words:
        sentence.append(random.choice(content))
        count+= 1

    for word in sentence:
        print(word)
    # print(*sentence) # using a "*" removes the weird syntax you usually see when printing a list
