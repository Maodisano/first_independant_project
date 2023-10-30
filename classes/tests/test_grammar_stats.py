from lib.grammar_stats import *
import pytest 

# given a valid sentance - capital letter and full stop 
# returns True
def test_if_sentance_is_valid_with_capital_and_stop():
    grammar_stats = GrammarStats()
    assert grammar_stats.check("Hello, this is a fine day.") == True

# given a sentance with capital letter and question mark - 
# returns True


def test_if_sentance_is_valid_with_capital_and_question():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hi, can i help?")
    assert result == True

# given a sentance with capital letter and exclamation mark - 
# returns True

def test_if_sentance_is_valid_with_capital_and_exclamation():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("This is the greatest day !")
    assert result == True

# given a text with capital and no suitable punctuation
# returns False

def test_if_sentance_is_valid_with_capital_and_no_punctuation():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("This is not cool")
    assert result == False

# given a text with no capital but suitable punctuation
# return False

def test_if_sentance_is_valid_with_no_capital_but_punctuation():
    grammar_stats = GrammarStats()
    assert grammar_stats.check("i dont know why i can't write.") == False

# given an empty text - will raise an error

def test_if_string_is_empty():
    grammar_stats = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar_stats.check("")
    error_message = str(e.value)
    assert error_message == "Cannot check grammar of empty string"

# given a test that passes the check 
# return 100 % 
# given 4 tests with half passing 

def test_with_passing_test_returning_100():
    grammar_stats= GrammarStats()
    grammar_stats.check("This is the greatest day !")
    grammar_stats.check("This is also good?")
    grammar_stats.check("not this")
    grammar_stats.check("or this")

    assert grammar_stats.percentage_good() == 50.0
