import pytest
from lib.reminder_with_error import *

"""
Throws exception when no reminder is added.
"""

def test_reminder():
    reminder = Reminder("Nathan")
    with pytest.raises(Exception) as e:
        reminder.remind()
    error_message = str(e.value)
    assert error_message == "No reminder set!"