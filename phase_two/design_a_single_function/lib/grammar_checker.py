def grammar_checker(text):
    if not text:
        return False
    elif text[0].isupper() and text[-1] in '.?!':
        return True
    else:
        return False 
    
    