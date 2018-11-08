 # module for generating histograms from a list of tokens
import cleanup # clean up source file
import tokenizer # turn source file into list of tokens
import sys # for command line args

def histogramDict(list_of_tokens):
    histogram = {} # create empty dictionary
    for word in list_of_tokens:
        if word not in histogram:
            # add to dictionary
            histogram[word] = 1
        else:
            # already exists in dictionary, so increment counter at that key
            histogram[word] += 1
    return histogram # return a data structure that stores ea. unique word & of times the word appears

if __name__ == '__main__':
    params = sys.argv[1:] # take a list of arguments, starting from index 1 till the end
    source_text = str(params[0]) # url for source_text
    content = cleanup.readFile(source_text)
    list_of_tokens = tokenizer.listOfTokens(content)
    histogram = histogramDict(list_of_tokens)
    print(histogram)
