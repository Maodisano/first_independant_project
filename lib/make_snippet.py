
def make_snippet(string):

    check_string_length = string.count(" ")+1
    if check_string_length > 5:
        split_string = ' '.join(string.split(' ', 5)[:5])
        return f"{split_string} ..."
    else:
        return string
