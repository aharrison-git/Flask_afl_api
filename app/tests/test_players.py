import json
import logging
import pytest
from test_data import player as test_data_player
from flask import request
LOGGER = logging.getLogger(__name__)


def test_get_all_players(client, test_data, access_token):
    headers = {"Authorization": "Bearer " + access_token}
    response = client.get('/api/v1/players', headers=headers)
    response_body = json.loads(response.get_data("as_text"))
    team_data = response_body["players"][0]
    LOGGER.info("response: {}".format(response_body))
    assert "msg" not in response_body
    assert response_body["count"] == 1, "There should be only one player"
    assert team_data["id"] == 1
    assert team_data["first_name"] == test_data_player["first_name"]
    assert team_data["last_name"] == test_data_player["last_name"]
    assert team_data["dob"] == test_data_player["dob"]
    assert team_data["matches_played"] == test_data_player["matches_played"]
    assert team_data["team_id"] == test_data_player["team_id"]
    assert team_data["career_goals"] == test_data_player["career_goals"]


def test_get_all_players_no_token(client, test_data):
    response = client.get('/api/v1/players')
    LOGGER.debug(f"test_players_token request: {request.url}")
    response_body = json.loads(response.get_data("as_text"))
    LOGGER.info("response: {}".format(response_body))
    assert response_body["msg"] == "Missing Authorization Header"



def test_add_player(client, test_data, access_token):
    headers = {"Authorization": "Bearer " + access_token, "Content-Type": "application/json"}
    first_name = "Fred"
    last_name = "Flinstone"
    request_data = {
        "first_name": first_name,
        "last_name": last_name,
        "dob": "1980-05-23",
        "matches_played": 154,
        "team_id": 1,
        "career_goals": 93
    }
    # check for success response
    response = client.post('/api/v1/players', data=json.dumps(request_data), headers=headers)
    response_body = json.loads(response.get_data("as_text"))
    LOGGER.info("response: {}".format(response_body))
    assert response_body["message"] == "Player " + first_name + " " + last_name + " has been created successfully."


    # check to see if team has been added
    response = client.get('/api/v1/players', headers=headers)
    response_body = json.loads(response.get_data("as_text"))
    LOGGER.info("response: {}".format(response_body))
    assert response_body["count"] == 2
    assert response_body["players"][1]["first_name"] == first_name

