# Estimate Reading Time of Text Function Design Recipe

## 1. Describe the Problem
As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.

 ```python

def est_reading_time(texts):
    # Parameters: 
    #   text: a string containing words (e.g. "This is a piece of text").
    # Returns: 
    #   an integer, reprsenting the estimated time to read the given text.
    #   E.g 10
    # Side effects: (state any side effects)
    #   This function doesn't print anything or have any other side-effects
  
    pass # Test-driving means _not_ writing any code here yet.
```
## 3. Create Examples as Tests

```Python

"""
Given a text of empty words, time to read would be 0.
"""
est_reading_time("") => 0

"""
Given a text of 200 words, time to read would be 1.
"""
est_reading_time("Hello " * 200) => 1

"""
Given a text of 150 words, time to read would be 1.
"""
est_reading_time("Hello " * 150) => 1

"""
Given a text of 400 words, time to read would be 2.
"""
est_reading_time("Hello " * 400) => 2

"""
Given a text of 25,000 words, time to read would 
"""
est_reading_time("Hello " * 25000) => 125

"""
Given a text that uses punctuation, only words are counted.

"""
est_reading_time("Hello, ! " * 200) => 1

"""
Given a text that is not a string type. An error is thrown.
"""
est_reading_time(None) throws an error
Encode each example as a test. You can add to the above list as you go.

```
4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

Here's an example for you to start with:

# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
Ensure all test function names are unique, otherwise pytest will ignore them!