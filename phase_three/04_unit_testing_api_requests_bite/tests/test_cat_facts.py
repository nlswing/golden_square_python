from unittest.mock import Mock
from lib.cat_facts import CatFacts

def test_cat_fact_api_returns_cat_fact():
    requester_mock = Mock()
    response_mock = Mock()
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"fact":"A happy cat holds her tail high and steady.","length":43}
    
    cat_fact = CatFacts(requester_mock)
    result = cat_fact.provide()
    assert result == "Cat fact: A happy cat holds her tail high and steady."
