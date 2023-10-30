


def get_most_common_letter(text):

    counter = {} # dictionary 

    for char in text:
        if char.isalpha():
            counter[char] = counter.get(char, 0) + 1 #getting the value of secified key
        # checking how many times we see the characters 2 = 1 time, 3 = twice
        # is also checking spaces and commas
        # creates a dictionary of the characters in string and how many times they are seen


    letter = sorted(counter.items(), key=lambda item: item[1])[-1][0] 
    # [10] is incorrect becuase it does not work with other strings
    # only finds the correct index because i can see the results
    # [0] [1] return item 0 of dict - return index 1 in item
    
    print("before key")
    print(counter.items())
    print("after key")
    print(sorted(counter.items(), key=lambda item: item[1]))
    # item: item[1] - sorts in order of least to most 
    
    return letter

#  returning intiger instead of letter

print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")
