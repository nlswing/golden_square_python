from lib.reminder import *

def test_reminds_the_user_to_do_a_task():
    reminder = Reminder('Nathan')
    reminder.remind_me_to('Put the washing out')
    result = reminder.remind()
    assert result == 'Put the washing out, Nathan!'