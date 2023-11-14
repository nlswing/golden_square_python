def make_snippet(words):
    if len(words.split()) <= 5:
        return words
    else:
        split_words = words.split()
        first_five_words = split_words[0:5]
        create_string = ' '.join(first_five_words)
        return create_string + '...'