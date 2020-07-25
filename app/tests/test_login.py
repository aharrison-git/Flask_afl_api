import json
import logging
import pytest

LOGGER = logging.getLogger(__name__)

def test_valid_user(client, test_data):
    data = {"username": "test_user", "password":"test1234"}
    headers = {"content-type": "application/json"}
    response = client.post('api/v1/user/login', data=json.dumps(data), headers=headers, follow_redirects=True)
    LOGGER.info(response.get_data(["as_text"]))
    response_json = json.loads(response.get_data())
    LOGGER.debug("json: {}".format(response_json["access_token"]))
    assert response.status_code == 200
    assert "access_token" in response_json
    assert len(response_json["access_token"]) > 50


def test_invalid_user(client, test_data):
    data = {"username": "fake_user", "password":"test1234"}
    headers = {"content-type": "application/json"}
    response = client.post('api/v1/user/login', data=json.dumps(data), headers=headers, follow_redirects=True)
    LOGGER.info(response.get_data(["as_text"]))
    response_json = json.loads(response.get_data())
    LOGGER.debug("json: {}".format(response_json))
    assert response.status_code == 401
    assert response_json["message"] == "Bad username or password"


def test_incorrect_password(client, test_data):
    data = {"username": "test_user", "password":"bad_password"}
    headers = {"content-type": "application/json"}
    response = client.post('api/v1/user/login', data=json.dumps(data), headers=headers, follow_redirects=True)
    LOGGER.info(response.get_data(["as_text"]))
    response_json = json.loads(response.get_data())
    LOGGER.debug("json: {}".format(response_json))
    assert response.status_code == 401
    assert response_json["message"] == "Bad username or password"


def test_no_password(client, test_data):
    data = {"username": "test_user"}
    headers = {"content-type": "application/json"}
    response = client.post('api/v1/user/login', data=json.dumps(data), headers=headers, follow_redirects=True)
    LOGGER.info(response.get_data(["as_text"]))
    response_json = json.loads(response.get_data())
    LOGGER.debug("json: {}".format(response_json))
    assert response.status_code == 400
    assert response_json["message"] == "Missing password parameter"



def test_no_username(client, test_data):
    data = {"password": "test1234"}
    headers = {"content-type": "application/json"}
    response = client.post('api/v1/user/login', data=json.dumps(data), headers=headers, follow_redirects=True)
    LOGGER.info(response.get_data(["as_text"]))
    response_json = json.loads(response.get_data())
    LOGGER.debug("json: {}".format(response_json))
    assert response.status_code == 400
    assert response_json["message"] == "Missing username parameter"

