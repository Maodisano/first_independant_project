from lib.time_to_read import *

# count number of words in text

#def test_count_number_of_words_in_text():
#    result = time_to_read("matteo is really brainy and has good code")    
#    assert 


# input empty string > expect 0 

def test_returns_empty_string():
    result = time_to_read("")
    assert result == 0

# inpute string > expect time taken  as intiger 
#def test_input_string_returns_time_taken():
#    result = time_to_read("matteo is really brainy and has good code")
#   assert result == 2.4

# input string > expect a time taken in sec  (think about how we calculate time)
def test_string_returns_time_in_secodnds():
    result = time_to_read("matteo is really brainy and has good code but is")
    assert result == "3.0 seconds" 






