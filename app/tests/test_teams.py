import json
import logging

LOGGER = logging.getLogger(__name__)


def test_get_all_teams(client, test_data, access_token):
    headers = {"Authorization": "Bearer " + access_token}
    response = client.get('/api/v1/teams', headers=headers)
    response_body = json.loads(response.get_data("as_text"))
    team_data = response_body["teams"][0]
    LOGGER.info("response: {}".format(response_body))
    assert "msg" not in response_body
    assert response_body["count"] == 1, "There should be only one team"
    assert team_data["id"] == 1
    assert team_data["location"] == "Victoria"
    assert team_data["name"] == "North Melbourne"
    assert team_data["premierships"] == 4
    assert team_data["wooden_spoons"] == 5
    assert team_data["years_in_afl"] == 113


def test_get_all_teams_no_token(client, test_data):
    response = client.get('/api/v1/teams')
    response_body = json.loads(response.get_data("as_text"))
    LOGGER.info("response: {}".format(response_body))
    assert response_body["msg"] == "Missing Authorization Header"


def test_add_team(client, test_data, access_token):
    headers = {"Authorization": "Bearer " + access_token, "Content-Type": "application/json"}
    team_name = "Essendon"
    request_data = {
        "name": team_name,
        "premierships": 12,
        "wooden_spoons": 7,
        "location": "Melbourne",
        "years_in_afl": 104
    }
    response = client.post('/api/v1/teams', data=json.dumps(request_data), headers=headers)
    response_body = json.loads(response.get_data("as_text"))
    LOGGER.info("response: {}".format(response_body))
    assert response_body["message"] == "Team " + team_name + " has been created successfully."


    # check to see if team has been added
    response = client.get('/api/v1/teams', headers=headers)
    response_body = json.loads(response.get_data("as_text"))
    LOGGER.info("response: {}".format(response_body))
    assert response_body["count"] == 2
    assert response_body["teams"][1]["name"] == team_name

