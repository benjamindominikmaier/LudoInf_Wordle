#!/usr/bin/env python3.9
# -*- coding: utf-8 -*

import random
import string
import operator
import argparse
from collections import Counter
from itertools import chain


### Setup ###
def retrieve_words(path: str, word_length: int=5) -> list:
    """
    Retrieve a word list with words of given length from a text file

    :param path: path of word list as str
    :param word_length: word length
    :returns: processed_words of given length
    :rtype: list
    """
    dict = open(path, "r")
    words = dict.readlines()

    processed_words = []
    for word in words:
        word = word.replace("\n","")
        if len(word) == word_length:
            processed_words.append(word.upper())
    dict.close()
    return processed_words


### Word prediction
def find_best_word(words: list, characters: list) -> str:
    """
    Determines best word based on single-character entropy optimization

    :param words: list of all possible words
    :param characters: list of all allowed characters
    :returns: word recommendation based on single-character entropy
    :rtype: str
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
    min_word = None

    for word in words:
        temp_word_value = 0
        for character in word:
            try:
                temp_word_value += result_dict[character]
            except:
                temp_word_value = 9999999999999999
        if len(set(word)) < len(word):
            temp_word_value += 5000 * (len(word) - len(set(word)))
        if temp_word_value < min_value:
            # print("Better word found with value ", temp_word_value)
            min_value = temp_word_value
            min_word = word
    #print(min_word, min_value)
    if min_word != None:
        return min_word
    else:
        raise ValueError('No word found!')


def update_wordlist(words: list, characters: list, user_input: str,
                    user_response: str):
    """
    Updates word list based on submitted word and wordle response

    :param words: list of all possible words
    :param characters: list of all allowed characters
    :param user_input: word the user submitted to wordle
    :param user_response: response to word from wordle
    :returns: updated word- and character-lists
    :rtype: (list, list)
    """
    updated_words = words.copy()

    # check if doubled letters appear in word (user_input)
    if len(set(user_input)) < len(user_input):
        print("Warning: Unstable for repeated characters")
        #raise NotImplementedError


    # iterate over all positions of the input word (user_input)
    for character_index in range(len(user_input)):
        # if character is correct, remove all words not having the character at
        # the respective position
        if user_response[character_index] == "G":
            for word in words:
                if user_input[character_index] != word[character_index]:
                    if word in updated_words:
                        updated_words.remove(word)
        elif user_response[character_index] == "Y":
            # if character appears at a different position, remove all words that
            # (a) do not contain that character
            # (b) contain the character at the respective position
            for word in words:
                if (user_input[character_index] == word[character_index]) or (user_input[character_index] not in word):
                    if word in updated_words:
                        updated_words.remove(word)
        elif user_response[character_index] == "?":
            # if character does not appear in the word, remove all words that
            # contain the respective character and remove the character from the
            # possible character list
            if user_input[character_index] in characters:
                characters.remove(user_input[character_index])
            for word in words:
                if user_input[character_index] in word:
                    if word in updated_words:
                        updated_words.remove(word)
        else:
            raise ValueError(f"Character {user_response[character_index]} not known. Valid options ['G', 'Y', '?']")
    return updated_words, characters


def solve(word_list_path: str="words_alpha.txt",
          allowed_characters: list=list(set(string.ascii_letters)),
          word_length: int=5,
          allowed_attempts: int=6) -> None:
    """
    Iterative interactive script to solve wordle

    1. obtain possible words
    2. add all characters as possible characters for each position
    3. iterate through attempts
        3.1 display best words
        3.2 ask user which word she/he tried
        3.3 ask user for response
        3.4 remove impossible characters
        3.5 update possible words

    :param word_list_path: file path to the word list with all possible words
    :param allowed_characters: list of all allowed characters (usually A-Z)
    :param word_length: length of searched word
    :param allowed_attempts: number of allowed attempts
    :rtype: None
    """
    status = "ongoing"
    words = retrieve_words(word_list_path, word_length)
    characters = allowed_characters.copy()
    for attempt in range(1,allowed_attempts+1):
        print(f"Attempt: {attempt}")
        print(f"Best Word is: {find_best_word(words, characters )}")
        user_input = input_word(words, word_length)
        user_response = input_response(word_length)
        if set(user_response) == set("G"):
            print("Congrats!")
            status = "win"
            break
        words, characters = update_wordlist(words, characters, user_input, user_response)
    if status == "ongoing":
        print("Schade!")
    print("Looking forward to see you tomorrow!")


### User interface ###
def input_word(word_list: list, word_length: int) -> str:
    """
    Ask user to input word in command line and return word if the word
    in word list and of right length

    :param word_list: list with all possibble words
    :param word_length: length of searched word
    :returns: word the user submitted to wordle
    :rtype: str
    """
    while True:
        word = input("Input the word you entered> ")
        if len(word) == word_length and word.upper() in word_list:
            return word.upper()


def input_response(word_length: int) -> str:
    """
    Ask user to input response from wordle in command line and return response
    if the response is of right length and only contains allowed characters

    :param word_length: length of searched word
    :returns: wordle response to input word entered by user
    :rtype: str
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
def benchmark(possible_words, allowed_characters):
    """
    Perform automatic benchmark routine to test different solving strategies

    :param possible_words:
    :param allowed_characters:
    :param word_length:
    :param allowed_attempts:
    :returns:
    :rtype:
    """
    best_word = find_best_word()
    for i in range(10000):
        test_word = random.sample(possible_words, 1)
        for word in possible_words:
            for character in test_word:
                for word_character in word:
                    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Calc identity", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--input_file', type=str, default="words_alpha.txt", help='file path to word list')
    parser.add_argument('--L', type=int, default=5, help='Word length')
    parser.add_argument('--N', type=int, default=6, help='Allowed solving attempts')
    parser.add_argument('--characters', nargs='+', type=int, default=list(set(string.ascii_letters)), help='list of allowed characters')

    args = parser.parse_args()

    solve(word_list_path=args.input_file, allowed_characters=args.characters,
          word_length=args.L, allowed_attempts=args.N)
