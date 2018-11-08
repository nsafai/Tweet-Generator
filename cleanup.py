# module for cleaning up source text and turning text into a list of tokens
import random # to generate random numbers
import re # for regular expressions
import sys # for command line args

def readFile(url):
    file = open(url, 'r')
    content = file.read().lower()
    clean_content = re.sub(r'\W+', ' ', content) # By Python definition '\W == [^a-zA-Z0-9_], which excludes all numbers, letters and _
    file.close()
    return clean_content

if __name__ == '__main__':
    params = sys.argv[1:] # take a list of arguments, starting from index 1 till the end
    source_text = str(params[0]) # url for source_text
    content = readFile(source_text)
    print(content)
