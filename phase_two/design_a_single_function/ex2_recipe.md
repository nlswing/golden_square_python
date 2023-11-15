# Estimate Reading Time of Text Function Design Recipe

## 1. Describe the Problem
As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.

 ```python

def grammar_check(texts):
    # Parameters: 
    #   text: a string containing words (e.g. "This is a piece of text").
    # Returns: 
    #   a boolean, True if the text starts with a caopital letter and ends with a suitable sentence-ending, False otherwise.
    #   E.g True
    # Side effects: (state any side effects)
    #   This function doesn't print anything or have any other side-effects
  
    pass # Test-driving means _not_ writing any code here yet.
```
## 3. Create Examples as Tests

```Python

"""
Given a text of empty words, the return would be False
"""
grammar_checker("") => False

"""
Given a text that starts with a capital letter and ends with a full stop, the return would be True.
"""
grammar_checker("This is a sentence.") => True

"""
Given a text that starts with a capital letter but does not end with valid punctuation, the return would be False.
"""
grammar_checker("This is a sentence,") => False

"""
Given a text that starts with a capital letter and ends with another valid punctuation mark, the return would be True.
"""
grammar_checker("This is a sentence!") => True

"""
Given a text that starts with a lower-case letter, the return would be False.
"""
grammar_checker("this is a sentence.") => False


"""
Given a text that is not a string type. An error is thrown.
"""
grammar_checker(None) throws an error
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