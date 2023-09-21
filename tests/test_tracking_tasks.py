from lib.tracking_tasks import *
import pytest 



# if the todo is capitalized - returns True

def test_if_text_contains_formatted_todo():
    result = tracking_tasks("I dont know what #TODO")
    assert result == True

# if todo is in the worng format - return false

def test_if_text_contains_wrong_formatted_todo():
    result = tracking_tasks("This string contains TODO")
    assert result == False

# if the text contains hastag but is not in the correct place 
# returns False

def test_with_hastag_in_wrong_place():

    result = tracking_tasks("This string contains TODO#")
    assert result == False

# if there are multiple #todo's
# returns True 

def test_with_multiple_todos():
    result = tracking_tasks("#TODO wash the dog, #TODO wash the car")
    assert result == True

# Vif the "todo" is not capitalized 
# returns False 

def test_with_lowercase_todo():
    result = tracking_tasks("I dont know what #todo")
    assert result == False

# check if the string is empty - should raise an exception
# returns - cannot check an empty string ""

def test_with_empty_string():

    with pytest.raises(Exception) as e:
        tracking_tasks("")
    error_message = str(e.value)
    assert error_message == "Cannot find string"
    
    








