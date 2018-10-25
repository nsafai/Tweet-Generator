import sys # to access command line arguments
import random # to generate random numbers
import itertools # to generate anagrams

def reversed_string(any_string):
    return any_string[::-1]

def generate_anagrams(any_string):
    return ["".join(perm) for perm in itertools.permutations(words[2])]

def shuffle_from_scratch(words):

    shuffled_array = []
    word_index = 0

    while len(words) != 0:
        random_index = random.randint(0, len(words)-1)
        shuffled_array.append(words[random_index])
        words.pop(random_index)
        word_index += 1

    return shuffled_array

if __name__ == '__main__':
    words = sys.argv[1:] # take a list of arguments, starting from index 1 till the end

    shuffled_array = shuffle_from_scratch(words)
    print(shuffled_array)
    # words[1] = reversed_string(words[1])
    # words[2] = generate_anagrams(words[2])
