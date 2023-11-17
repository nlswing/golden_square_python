import math
import re

def est_reading_time(text):
    if isinstance(text, str):
        remove_non_letters = re.split(r"\W+", text)
        remove_empty_strings = [word for word in remove_non_letters if word]
        # reading speed is 200 pm
        reading_speed = 200
        calculate_time_to_read = len(remove_empty_strings) / reading_speed
        return math.ceil(calculate_time_to_read)
    else:
        raise Exception("Invalid input. Please use a text of string type")