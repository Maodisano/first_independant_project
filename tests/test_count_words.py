from lib.count_words import *
# plan - create a function that takes a string as an argument,
# returns the number of words in that string

"""
first - check that a string can be taken as an argument
"""

#def test_takes_string_as_an_argument_returns_empty_string():
#    result = count_words("string")
#    assert result == "string"

"""
next check that the program can count the number of words in a string

"""

def test_how_many_words_in_string_returns_intiger():
    result = count_words("Hello world my name is matteo")
    assert result == 6