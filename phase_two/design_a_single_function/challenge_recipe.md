# Check for TODO in Text Function Design Recipe

## 1. Describe the Problem
As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.

## 2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.

 ```python

def check_todo(text):
    # Parameters: 
    #   text: a string containing words (e.g. "This is a piece of text").
    # Returns: 
    #   a boolean, True if the text include the string #TODO, False otherwise.
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
check_todo("") => False

"""
Given a text that includes the string #TODO, it will return True.
"""
check_todo("#TODO take the bins out.") => True

"""
Given a text that does not include #TODO, it returns False.
"""
check_todo("Take bins out.") => False

"""
Given a text that contains TODO, it would return False.
"""
check_todo("Todo take bins out!") => False

"""
Given a text that contains #todo, it returns False.
"""
check_todo("#todo take bins out.") => False


"""
Given a text that just contains #TODO, it return True.
"""
check_todo("#TODO") => True
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