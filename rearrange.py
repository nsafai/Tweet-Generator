import sys # to access command line arguments
import random # to generate random numbers
import itertools # to generate anagrams

def reversed_string(any_string):
    return any_string[::-1]

def generate_anagrams(any_string):
    return ["".join(perm) for perm in itertools.permutations(params[2])]

if __name__ == '__main__':
    params= sys.argv[1:] # take a sublist starting from index 1 till the end
    random.shuffle(params)
    params[1] = reversed_string(params[1])
    params[2] = generate_anagrams(params[2])
    print(params)
