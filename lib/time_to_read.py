
def time_to_read(text):
    text_word_count = text.count(" ")+1
    if text == "":
        return 0
    else:
        time_taken = 60/(200/text_word_count) 
        return f"{time_taken} seconds"




# 200 words in 1 min 
# 1 word in x 
# 60/(200/text_word_count)