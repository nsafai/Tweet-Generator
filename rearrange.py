import sys # to access command line arguments
import random # to generate random numbers

def reversed_string(a_string):
    return a_string[::-1]

if __name__ == '__main__':
    params= sys.argv[1:] # take a sublist starting from index 1 till the end
    random.shuffle(params)
    params[1] = reversed_string(params[1])
    print(params)
