import json
import logging
import pytest
from test_data import player as test_data_player

LOGGER = logging.getLogger(__name__)

data_update = {
    "id": 1,
    "first_name": "Barney",
    "last_name": "Rubble",
    "dob": "1991-02-25",
    "matches_played": 123,
    "career_goals": 66,
    "team_id": 1
}

def test_get_player_by_id(client, test_data, access_token):
    headers = {"Authorization": "Bearer " + access_token, "Content-Type": "application/json"}
    response = client.get('api/v1/players/' + str(data_update["id"]), headers=headers)
    LOGGER.debug(f"get_player - client: {client}")
    LOGGER.debug(f"get_player - response status code: {response.status_code}")
    response_body = json.loads(response.get_data("as_text"))
    LOGGER.info(f"response body: {response_body}")
    assert response_body["message"] == "success"
    assert response_body["player"]["player_id"] == data_update["id"]
    assert response_body["player"]["first_name"] == test_data_player["first_name"]
    assert response_body["player"]["last_name"] == test_data_player["last_name"]


def test_get_player_invalid_id(client, test_data, access_token):
    headers = {"Authorization": "Bearer " + access_token, "Content-Type": "application/json"}
    response = client.get('api/v1/players/99', headers=headers)
    assert response.status_code == 404


def test_put_player_by_id(client, test_data, access_token):
    headers = {"Authorization": "Bearer " + access_token, "Content-Type": "application/json"}
    request_data = {
        "first_name": data_update["first_name"],
        "last_name": data_update["last_name"],
        "dob": data_update["dob"],
        "matches_played": data_update["matches_played"],
        "team_id": 1,
        "career_goals": data_update["career_goals"]
    }
    response = client.put('api/v1/players/' + str(data_update["id"]), data=json.dumps(request_data), headers=headers)
    response_body = json.loads(response.get_data("as_text"))
    LOGGER.info(f"response body: {response_body}")
    assert response_body["message"] == "Player " + data_update["first_name"] + " " + data_update["last_name"] + " has been updated successfully."

    # check to see if player has been updated
    response = client.get('api/v1/players/' + str(data_update["id"]), headers=headers)
    response_body = json.loads(response.get_data("as_text"))
    LOGGER.info(f"response body: {response_body}")
    assert response_body["message"] == "success"
    assert response_body["player"]["player_id"] == data_update["id"]
    assert response_body["player"]["first_name"] ==data_update["first_name"]


def test_patch_player_by_id(client, test_data, access_token):
    headers = {"Authorization": "Bearer " + access_token, "Content-Type": "application/json"}
    matches = 321
    request_data = {
        "matches_played": matches
    }
    response = client.patch('api/v1/players/' + str(data_update["id"]), data=json.dumps(request_data), headers=headers)
    response_body = json.loads(response.get_data("as_text"))
    LOGGER.info(f"response body: {response_body}")
    assert response_body["message"] == "Player " + data_update["first_name"] + " " + data_update["last_name"] + " has been updated successfully."

    # check to see if player has been updated
    response = client.get('api/v1/players/' + str(data_update["id"]), headers=headers)
    response_body = json.loads(response.get_data("as_text"))
    LOGGER.info(f"response body: {response_body}")
    assert response_body["message"] == "success"
    assert response_body["player"]["player_id"] == 1
    assert response_body["player"]["matches_played"] == matches



def test_delete_player_by_id(client, test_data, access_token):
    headers = {"Authorization": "Bearer " + access_token, "Content-Type": "application/json"}
    response = client.delete('api/v1/players/' + str(data_update["id"]), headers=headers)
    response_body = json.loads(response.get_data("as_text"))
    LOGGER.info(f"response body: {response_body}")
    assert response_body["message"] == "Player " + data_update["first_name"] + " " + data_update["last_name"] + " has been deleted successfully."

    # check to see if player has been deleted
    response = client.get('api/v1/players/' + str(data_update["id"]), headers=headers)
    assert response.status_code == 404

