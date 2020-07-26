import json
import logging
import pytest
from test_data import team as test_data_team

LOGGER = logging.getLogger(__name__)


def test_get_team_by_id(client, test_data, access_token):
    headers = {"Authorization": "Bearer " + access_token, "Content-Type": "application/json"}
    id = 1
    response = client.get('api/v1/teams/' + str(id), headers=headers)
    response_body = json.loads(response.get_data("as_text"))
    LOGGER.info(f"response body: {response_body}")
    assert response_body["message"] == "success"
    assert response_body["team"]["id"] == 1
    assert response_body["team"]["location"] == test_data_team["location"]
    assert response_body["team"]["name"] == test_data_team["name"]
    

def test_get_team_invalid_id(client, test_data, access_token):
    headers = {"Authorization": "Bearer " + access_token, "Content-Type": "application/json"}
    id = 99
    response = client.get('api/v1/teams/' + str(id), headers=headers)
    assert response.status_code == 404



def test_put_team_by_id(client, test_data, access_token):
    headers = {"Authorization": "Bearer " + access_token, "Content-Type": "application/json"}
    id = 1
    team_name = "Hawthorn"
    request_data = {
        "name": team_name,
        "premierships": 16,
        "wooden_spoons": 5,
        "location": "Melbourne",
        "years_in_afl": 101
    }
    response = client.put('api/v1/teams/' + str(id), data=json.dumps(request_data), headers=headers)
    response_body = json.loads(response.get_data("as_text"))
    LOGGER.info(f"response body: {response_body}")
    assert response_body["message"] == "Team Hawthorn successfully updated"

    # check to see if team has been updated
    response = client.get('api/v1/teams/' + str(id), headers=headers)
    response_body = json.loads(response.get_data("as_text"))
    LOGGER.info(f"response body: {response_body}")
    assert response_body["message"] == "success"
    assert response_body["team"]["id"] == 1
    assert response_body["team"]["name"] == team_name


def test_patch_team_by_id(client, test_data, access_token):
    headers = {"Authorization": "Bearer " + access_token, "Content-Type": "application/json"}
    id = 1
    years = 999
    request_data = {
        "years_in_afl": years
    }
    response = client.patch('api/v1/teams/' + str(id), data=json.dumps(request_data), headers=headers)
    response_body = json.loads(response.get_data("as_text"))
    LOGGER.info(f"response body: {response_body}")
    assert response_body["message"] == "Team Hawthorn successfully updated"

    # check to see if team has been updated
    response = client.get('api/v1/teams/' + str(id), headers=headers)
    response_body = json.loads(response.get_data("as_text"))
    LOGGER.info(f"response body: {response_body}")
    assert response_body["message"] == "success"
    assert response_body["team"]["id"] == 1
    assert response_body["team"]["years_in_afl"] == years



def test_delete_team_by_id(client, test_data, access_token):
    headers = {"Authorization": "Bearer " + access_token, "Content-Type": "application/json"}
    id = 1
    response = client.delete('api/v1/teams/' + str(id), headers=headers)
    response_body = json.loads(response.get_data("as_text"))
    LOGGER.info(f"response body: {response_body}")
    assert response_body["message"] == "Team Hawthorn successfully deleted"

    # check to see if team has been deleted
    response = client.get('api/v1/teams/' + str(id), headers=headers)
    assert response.status_code == 404