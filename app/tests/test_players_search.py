import json
import logging
import pytest
from test_data import player as test_data_player

LOGGER = logging.getLogger(__name__)


@pytest.mark.parametrize("search_parameter", ["first_name", "last_name", "dob", "matches_played", "career_goals"])
def test_player_get_search(client, test_data, access_token, search_parameter):
    headers = {"Authorization": "Bearer " + access_token, "Content-Type": "application/json"}
    request_data = {search_parameter: test_data_player[search_parameter]}
    response = client.get('api/v1/players/search', query_string=request_data, headers=headers)
    response_body = json.loads(response.get_data("as_text"))
    LOGGER.info(f"response body: {response_body}")
    assert response_body["players"][0][search_parameter] == test_data_player[search_parameter]



def test_player_get_search_by_invalid_name(client, test_data, access_token):
    headers = {"Authorization": "Bearer " + access_token, "Content-Type": "application/json"}
    request_data = {"first_name": "Testy McTestface"}
    response = client.get('api/v1/players/search', query_string=request_data, headers=headers)
    response_body = json.loads(response.get_data("as_text"))
    LOGGER.info(f"response body: {response_body}")
    assert response_body["count"] == 0
    assert len(response_body["players"]) == 0



@pytest.mark.parametrize("search_parameter", ["first_name", "last_name", "dob", "matches_played", "career_goals"])
def test_player_post_search(client, test_data, access_token, search_parameter):
    headers = {"Authorization": "Bearer " + access_token, "Content-Type": "application/json"}
    request_data = {search_parameter: test_data_player[search_parameter]}
    response = client.get('api/v1/players/search', data=json.dumps(request_data), headers=headers)
    response_body = json.loads(response.get_data("as_text"))
    LOGGER.info(f"response body: {response_body}")
    assert response_body["players"][0][search_parameter] == test_data_player[search_parameter]



def test_player_post_search_by_invalid_name(client, test_data, access_token):
    headers = {"Authorization": "Bearer " + access_token, "Content-Type": "application/json"}
    request_data = {"first_name": "Fakey McFakeface"}
    response = client.post('api/v1/players/search', data=json.dumps(request_data), headers=headers)
    response_body = json.loads(response.get_data("as_text"))
    LOGGER.info(f"response body: {response_body}")
    assert response_body["count"] == 0
    assert len(response_body["players"]) == 0    