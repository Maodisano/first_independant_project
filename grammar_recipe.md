# time_to_read recipe

# 1. Describe the problem:

# _Put or write the use story here. Add any clarifying notes you might have._ 

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.



# 2. Design the function signature:
# _Include the name of the function, its parameters, return value and side effects._ 

def check_writing_accuracy(text):

> parameters:

>text: a string representing text
> check capital letter at the start
> check if text ends with suitable punctuation

> ?boolean - true or false to assert whether parameters are met




# 3. Create examples examples as tests:

test 1

given a sentance with capital letter and full stop -
will return a boolean > True

check_writing_accuracy( "Hello, this is a fine day. ):
> True

test 2
given a sentance with capital letter and question mar - 
returns True

check_writing_accuracy( "Hi, can i help? "):
> True

test 3

given a text with capital letter and exclamation mark 
> True

check_writing_accuracy( This is the greates day ! ):
> True

test 4

given a text with capital and no suitable punctuation
> False

check writing_accuracy( This is not cool )
>False

test 5

given a text with no capital but suitable punctuation
> False

check_writing_accuracy ( i dont know why i can't write. )
> False

test 6

given an empty text - will raise an error

check_writing_accuracy( ? )
Raises exception
"Cannot check grammar of empty string"













    