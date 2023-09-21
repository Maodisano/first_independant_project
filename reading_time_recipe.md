# time_to_read recipe

# 1. Describe the problem:

# _Put or write the use story here. Add any clarifying notes you might have._ 

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, 
assuming that I can read 200 words a minute.


# 2. Design the function signature:
# _Include the name of the function, its parameters, return value and side effects._ 

python
def estimate_reading_time(text)
> parameters:
> text; a string representing human-readable text
>Return:
> a float representing reading time

# 3. Create examples examples as tests:

given a text f 200 words
it will return a reading time of 1

estimate_reading_time(" 200 ")
> 1.0


given a reading time of 400 words
it will return a reading time of 2

estimate_reading_time( " 400 ")
> 2.0

given a reading time of 300 words
it will return areading time of 1.5

estimate_reading_time(" 300 ")
>1.5

given an empty text 
it will raise an error

estimate_reading_time(" ")
>raises error _-

make words syntax:
text = " ".join(["word" for i in range(0, 200)])






    