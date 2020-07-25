import pytest
from flask import g
from app import create_app, db
from app.config import app_config, TestingConfigDB
import os
import tempfile
import logging
from werkzeug.security import generate_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from app.model.teams import TeamModel
from test_data import team

LOGGER = logging.getLogger(__name__)

@pytest.fixture(scope="module")
def client():
    """Initialize app, return test_client object."""
    
    app = create_app(config_class=app_config["testing"])
    app.config.from_object(TestingConfigDB)
    with app.test_client() as client:
        with app.app_context():
            db.drop_all()
            db.create_all() # create all tables
            db.session.commit()
            yield client
        


@pytest.fixture(scope="module")
def test_data():
    # create test user
    password_hash = generate_password_hash("test1234")
    sql = "INSERT INTO users (username, password) VALUES ('%s', '%s)" % ('test_user', password_hash + '\'')
    result_proxy = db.session.execute(sql)
    db.session.commit()

    # create team
    sql = "INSERT INTO team (name, location, premierships, wooden_spoons, years_in_afl) VALUES ('%s', '%s', %d, %d, %d)" \
            % (team["name"], team["location"], team["premierships"], team["wooden_spoons"], team["years_in_afl"])
    db.session.execute(sql)
    db.session.commit()
            
    # create player
    team_id = TeamModel.query.first().id
    sql = "INSERT INTO player (first_name, last_name, dob, matches_played, team_id, career_goals) VALUES ('%s', '%s', '%s', %d, %d, %d)" \
       % ("test_first", "test_last", "13-04-1991", 58, team_id, 147)
    db.session.execute(sql)
    db.session.commit()


@pytest.fixture()
def access_token():
    # login and return token
    access_token = create_access_token(identity="test_user")
    return access_token