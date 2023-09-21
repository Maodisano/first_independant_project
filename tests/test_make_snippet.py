from lib.make_snippet import *

"""
Given a string as an argument, return the string
"""

def test_input_string_returns_the_string():
    result = make_snippet("Hello world I am Matteo")
    assert result == "Hello world I am Matteo"

"""
check how many words are in the string
"""

#def test_how_many_words_in_string():
#    result = make_snippet("Hello world I am Matteo Di Santolo")
#    assert result == 7


"""
Given a string thats longer than 5 words, return the first five words of that string followed by " ... "

"""

def test_return_first_five_words_of_string():
    result = make_snippet("Hello world i would like some luck")
    assert result == "Hello world i would like ..."
