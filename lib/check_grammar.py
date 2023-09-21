
def check_writing_accuracy(text):
    if text == "":
        raise Exception("Cannot check grammar of empty string")
    elif text[0].isupper() and text[-1] in ".?!":
        return True
    else:
        return False
    
    
