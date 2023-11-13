from lib.gratitudes import *

"""
Nothing is added to list so gatitudes are left blank.
"""

def test_nothing_added_returns_blank_gratitudes():
    gratitude = Gratitude()
    result = gratitude.format()
    assert result == "Be grateful for: "
    
"""
One gratitude is added and is returned in the correctly formatted way.
"""

def test_gratitude_is_returned_in_formatted_way():
    gratitude = Gratitude()
    gratitude.add('sunshine')
    result = gratitude.format()
    assert result == "Be grateful for: sunshine"
    
"""
Multiple gratitudes are added and returned, formatted in the expected way.
"""

def test__multiple_gratitudes_are_returned_in_formatted_way():
    gratitude = Gratitude()
    gratitude.add('sunshine')
    gratitude.add('bees')
    gratitude.add('music')
    result = gratitude.format()
    assert result == "Be grateful for: sunshine, bees, music"
