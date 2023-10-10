#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Python Group Da Nang"
__version__ = "0.1.0"
__license__ = "MIT"

# All our lists
error_list =["0","1","2","3","4","5","6","7","8","9"]
valid_list = ["I","X","C","M","V","L","D"]
aux_characters = ["V","L","D"]
basic_characters = ["I","X","C","M"]
convert_character ={"I": 1,"X":10,"C":100,"M":1000,"V":5,"L":50,"D":500}

def subtract_aux_check(characters):
    print("Pass")

def check_symbols(characters):
    print(type(characters))
    print("Check Symbols ", characters)
    # Check no number
    for character in characters:
        print(character)
        if character in error_list:
            print(" Please don't use Arabic numbers")
            break
        elif character not in error_list and character in valid_list:
            subtract_aux_check(characters)
        elif character not in valid_list:
            print(" Only these characters are valid I,V,X,L,C,D,M ")
            break

def main(characters):
    """ Main entry point of the app """
    check_symbols(characters)

while True:
    characters = input("Type in the Roman number: ")
    main(characters)