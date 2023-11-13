# We have to import the function we want to test first.
from lib.add_five import *

# Next, we create a single test example.
# The function name must start with `test_` for pytest to find it.
# The rest of the function should describe what the test verifies.
def test_add_five_returns_eight_for_three():
    # We run the function with an example argument 3.
    result = add_five(3)
    
    # And then assert that in this example it should return 8.
    assert result == 8
    
   # pytest will run this example, and if this example doesn't work like you
   # said it would, the test will fail. 