import re

def get_most_common_letter(text):
    counter = {}
    # Remove non-alpha characters.
    text = re.sub(r"[^a-zA-Z]", "", text)
    for char in text:
        counter[char] = counter.get(char, 0) + 1
    # Sorted by lowest value - swap [0] (1st element in dict) to [-1] last element. To get key swap [1] for [0].   
    letter = sorted(counter.items(), key=lambda item: item[1])[-1][0]
    
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")