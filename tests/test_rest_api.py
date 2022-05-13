import pytest
import requests

@pytest.mark.duckduckgo
@pytest.mark.rest_api
def test_duckduckgo_instant_answer_api():

    # Arrange
    url = "https://api.duckduckgo.com/?q=python+programming&format=json"

    # Act
    # sends the request as http get to the input
    response = requests.get(url)
    # parses response to a python dictionary action for validation
    body = response.json()

    # Assert
    # verify successful request
    assert response.status_code == 200
    #check the content of the response.
    # goood response shoudl have python somewher
    assert 'Python' in body['AbstractText']