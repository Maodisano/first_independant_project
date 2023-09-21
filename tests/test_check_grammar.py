from lib.check_grammar import *
import pytest 

# given a valid sentance - capital letter and full stop 
# returns True

def test_if_sentance_is_valid_with_capital_and_stop():

    result = check_writing_accuracy("Hello, this is a fine day.")
    assert result == True

# given a sentance with capital letter and question mark - 
# returns True

def test_if_sentance_is_valid_with_capital_and_question():

    result = check_writing_accuracy("Hi, can i help?")
    assert result == True

# given a sentance with capital letter and exclamation mark - 
# returns True

def test_if_sentance_is_valid_with_capital_and_exclamation():
    result = check_writing_accuracy("This is the greatest day !")
    assert result == True

# given a text with capital and no suitable punctuation
# returns False

def test_if_sentance_is_valid_with_capital_and_no_punctuation():

    result = check_writing_accuracy("This is not cool")
    assert result == False

# given a text with no capital but suitable punctuation
# return False

def test_if_sentance_is_valid_with_no_capital_but_punctuation():

    result = check_writing_accuracy("i dont know why i can't write.")
    assert result == False

# given an empty text - will raise an error

def test_if_string_is_empty():

    with pytest.raises(Exception) as e:
        check_writing_accuracy("")
    error_message = str(e.value)
    assert error_message == "Cannot check grammar of empty string"

    


