from unittest.mock import Mock
from lib.time_error import TimeError

# def test_calls_api_to_provide_time_error():
#     requester_mock = Mock(name="requester")
#     response_mock = Mock(name="response")
    
#     requester_mock.get.return_value = response_mock
#     response_mock.json.return_value = {"abbreviation":"GMT","client_ip":"82.44.2.32","datetime":"2023-11-22T11:25:40.192720+00:00","day_of_week":3,"day_of_year":326,"dst":False,"dst_from":None,"dst_offset":0,"dst_until":None,"raw_offset":0,"timezone":"Europe/London","unixtime":1700652340,"utc_datetime":"2023-11-22T11:25:40.192720+00:00","utc_offset":"+00:00","week_number":47}
    
#     time_mock = Mock()
#     time_mock.time().return_value = -473.847204208374
    
#     time_error = TimeError(requester_mock)
#     result = time_error.error()
#     assert result == 

def test_returns_difference_between_local_and_remote_times():
    # Set up request and response mock.
    requester_mock = Mock()
    response_mock = Mock()
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"unixtime":1700652340}
    # Set up time mock.
    timer_mock = Mock()
    timer_mock.time.return_value = 1700652340.5
    time_error = TimeError(requester_mock, timer_mock)
    assert time_error.error() == -0.5  