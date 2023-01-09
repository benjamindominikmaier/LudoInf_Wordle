#!/usr/bin/env python3.9
# -*- coding: utf-8 -*

import random
import string
import operator
from collections import Counter
from itertools import chain

DICT = "/usr/share/dict/american-english"

ALLOWABLE_CHARACTERS = set(string.ascii_letters)
#ALLOWABLE_CHARACTERS = set("A", "B", "C", ... "Z", "")
ALLOWED_ATTEMPTS = 6
WORD_LENGTH = 5


### Setup ###
def retrieve_words(path: str, word_length: int=5):
    """
    Retrieve a word list with words of given length from a text file

    :param path: path of word list as str
    :param word_length: word length
    :returns: processed_words of given length
    :rtype: list
    """
    dict = open(path, "r")
    words = dict.readlines()
    #print(len(words))
    processed_words = []
    for word in words:
        if len(word) == word_length+1:
            if word[0:-1].isalpha():
                processed_words.append(word[0:-1].upper())
    # print(processed_words[0:10], len(processed_words))
    dict.close()
    return processed_words


### Word prediction
def character_probability(words, characters):
    """

    """
    result_dict = dict()
    for character in characters:
        if character == character.upper():
            counter = 0
            for word in words:
                if character in word:
                    counter += 1
                else:
                    counter -= 1
            result_dict[character] = abs(counter)

    min_value = 9999999999
    min_word = "Schlecht"

    for word in words:
        temp_word_value = 0
        for character in word:
            try:
                temp_word_value += result_dict[character]
            except:
                temp_word_value = 9999999999999999
        if temp_word_value < min_value:
            print("Better word found with value ", temp_word_value)
            min_value = temp_word_value
            min_word = word
    print(min_word, min_value)
    return min_word


def solve():
    """
    1. obtain possible words
    2. add all characters as possible characters for each position
    3. iterate through attempts
        3.1 display best words
        3.2 ask user which word she/he tried
        3.3 ask user for response
        3.4 remove impossible characters
        3.5 update possible words

    :param:
    :param:
    :return:
    :rtype:
    """


    pass


### User interface ###
def input_word(word_list: list, word_length: int):
    """
    Ask user to input word in command line and return word if the word
    in word list and of right length

    :param word_list:
    :param word_length:
    :returns:
    :rtype:
    """
    while True:
        word = input("Input the word you entered> ")
        if len(word) == word_length and word.upper() in word_list:
            return word.upper()

    #word = input("Input the word you entered> ")
    #if len(word) == word_length and word.upper() in word_list:
    #    return word
    #else:
    #    return input_word(word_list, word_length)

# -> Vortrag Mengenlehre Clemens
def input_response(word_length):
    """
    """
    print("Type the color-coded reply from Wordle:")
    print("  G for Green")
    print("  Y for Yellow")
    print("  ? for Gray")

    while True:
        response = input("Response from Wordle> ")
        if len(response) == word_length:
            for pos in response:
                if pos in ["G", "Y", "?"]:
                    return response
                else:
                    print(f"Error - invalid answer {response}")
        else:
            print(f"Error - invalid answer {response}")


### Benchmark Routine ###
def benchmark(possible_words, ALLOWABLE_CHARACTERS):
    best_word = character_probability()
    for i in range(10000):
        test_word = random.sample(possible_words, 1)
        for word in possible_words:
            for character in test_word:
                for word_character in word:
                    pass

### Unit Test ### -> Vortrag (Mentorenteam)
# 1. Testfunktionen formulieren
# 2. Schreiben des Programmes
# =======
# 1. Code Schreiben
# 2. Ärgern, weil Code nicht funktioniert
# 3. Fehler nicht findern, weil keine Tests implementiert
# 4. Verzweifeln
# 5. Nun doch Tests schreiben

if __name__ == '__main__':
    possible_words = retrieve_words(DICT, WORD_LENGTH)
    character_probability(possible_words, ALLOWABLE_CHARACTERS)
