import json
import logging
import pytest
from test_data import team as test_data_team

LOGGER = logging.getLogger(__name__)


@pytest.mark.parametrize("search_parameter", ["name", "location", "premierships", "wooden_spoons", "years_in_afl"])
def test_team_get_search(client, test_data, access_token, search_parameter):
    headers = {"Authorization": "Bearer " + access_token, "Content-Type": "application/json"}
    request_data = {search_parameter: test_data_team[search_parameter]}
    response = client.get('api/v1/teams/search', query_string=request_data, headers=headers)
    response_body = json.loads(response.get_data("as_text"))
    LOGGER.info(f"response body: {response_body}")
    assert response_body["teams"][0][search_parameter] == test_data_team[search_parameter]

def test_team_get_search_by_invalid_name(client, test_data, access_token):
    headers = {"Authorization": "Bearer " + access_token, "Content-Type": "application/json"}
    request_data = {"name": "Springfield Isotopes"}
    response = client.get('api/v1/teams/search', query_string=request_data, headers=headers)
    response_body = json.loads(response.get_data("as_text"))
    LOGGER.info(f"response body: {response_body}")
    assert response_body["count"] == 0
    assert len(response_body["teams"]) == 0



@pytest.mark.parametrize("search_parameter", ["name", "location", "premierships", "wooden_spoons", "years_in_afl"])
def test_team_post_search(client, test_data, access_token, search_parameter):
    headers = {"Authorization": "Bearer " + access_token, "Content-Type": "application/json"}
    request_data = {search_parameter: test_data_team[search_parameter]}
    response = client.get('api/v1/teams/search', data=json.dumps(request_data), headers=headers)
    response_body = json.loads(response.get_data("as_text"))
    LOGGER.info(f"response body: {response_body}")
    assert response_body["teams"][0][search_parameter] == test_data_team[search_parameter]



def test_team_post_search_by_invalid_name(client, test_data, access_token):
    headers = {"Authorization": "Bearer " + access_token, "Content-Type": "application/json"}
    request_data = {"name": "Springfield Isotopes"}
    response = client.post('api/v1/teams/search', data=json.dumps(request_data), headers=headers)
    response_body = json.loads(response.get_data("as_text"))
    LOGGER.info(f"response body: {response_body}")
    assert response_body["count"] == 0
    assert len(response_body["teams"]) == 0    