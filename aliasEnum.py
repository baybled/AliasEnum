#! /usr/bin/python3

import re
import sys

'''
DEF: Enumerates aliases based on splitting current aliases into substrings and re-combining to show alternatives
'''

def split_alias(alias):
    # DEF: Takes input, splits in appropriate places
    
    # regex splits on numbers, lowercase, uppercase+lowercase, punctuation
    foundSplits = re.findall(r'[0-9]+|[a-z]+|[A-Z][a-z]+|[^\w\s]', alias)
    
    return foundSplits

def process_input(user_input):
    # DEF: Takes user input, splits and returns unique split options

    splits = []

    # go through each, splitting
    for each_alias in user_input:
        splits += split_alias(each_alias)

    # remove duplicates
    splits = list(dict.fromkeys(splits))

    # output
    enumerate_from_splits(splits)

def enumerate_from_splits(splits):
    # DEF: Takes split options, returns new combinations

    new_combinations = []

    # go through each, making new combinations
    for each_prefix in splits:
        for each_suffix in splits:
            if each_prefix != each_suffix:
                print('- '+each_prefix+each_suffix)
                new_combinations.append(each_prefix+each_suffix)

    print('\n'+'**'+str(len(new_combinations))+' values found**\n')

def operator(command_line_input):
    # DEF: Ensures running of program

    # remove program name from list
    command_line_input.pop(0)

    process_input(command_line_input)
    

if __name__ == '__main__':
    operator(sys.argv)
