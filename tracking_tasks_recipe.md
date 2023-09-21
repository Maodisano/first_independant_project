# tracking_tasks recipe

# 1. Describe the problem:

# _Put or write the use story here. Add any clarifying notes you might have._ 

As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.




# 2. Design the function signature:
# _Include the name of the function, its parameters, return value and side effects._ 

def tracking_tasks(text):

> parameters
> string - which is human-readable text 
> return a boolean - whether the text contains #TODO


# 3. Create examples examples as tests:

test 1 

check if the string is empty - should raise an exception
returns - cannot check an empty string ""

tracking_tasks("")
> Exception

test 2

if the text contains #TODO -
returns true

tracking_tasks("This string contains #TODO")
> True

test 3 

if the text contains TODO but without the # 
returns false 

tracking_tasks("This string contains TODO")
> False

test 4

if the text contains hastag but is not in the correct place 
returns False

tracking_tasks("This string contains TODO#")
> False

test 5

if the "TODO" is not capitalized 
returns False 

tracking_tasks("I dont know what todo")
> True

test 6

if there are multiple #TODO 's
returns True 

tracking_tasks("#TODO wash the dog, #TODO wash the car")
> True 













    