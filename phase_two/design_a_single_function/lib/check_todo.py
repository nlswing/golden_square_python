def check_todo(text):
    if text == "":
        return False
    elif '#TODO' in  text:
        return True
    
    return False
