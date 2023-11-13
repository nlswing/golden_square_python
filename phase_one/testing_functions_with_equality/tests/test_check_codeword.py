from lib.check_codeword import *

def test_check_codeword_incorrect_returns_wrong():
    result = check_codeword('bananas')
    assert result == 'WRONG!'
    
def test_check_codeword_close_returns_close():
    result = check_codeword('house')
    assert result == 'Close, but nope.'

def test_check_codeword_correct_returns_correct():
    result = check_codeword('horse')
    assert result == 'Correct! Come in.'
    
def test_with_wrong_first_letter_and_right_last_letter():
    result = check_codeword('mouse')
    assert result == 'WRONG!'