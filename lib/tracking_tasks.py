def tracking_tasks(text):
    if text == "":
        raise Exception("Cannot find string")
    elif "#TODO" in text:
        return True
    return False
    
