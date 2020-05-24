from flask import Flask
from app.config import app_config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import os


'''
#pre app factory version
app = Flask(__name__)
app.config.from_object(Config)
app.config.from_object(Configdb)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
'''


db = SQLAlchemy()  # done here so that db is importable
migrate = Migrate()


def create_app(config_class=app_config["development"]):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)
    with app.app_context():
        # Include our Routes
        from app.endpoints.teams import route
        from app.endpoints.teams.team import route
        from app.endpoints.teams.search import route
        from app.endpoints.players import route
        from app.endpoints.players.player import route
        from app.endpoints.players.search import route
        from app.model import teams
        from app.model import players
        return app

    

        

'''
from app.endpoints.teams import route
from app.endpoints.teams.team import route
from app.endpoints.teams.search import route
from app.endpoints.players import route
from app.endpoints.players.player import route
from app.endpoints.players.search import route
from app.model import teams
from app.model import players
'''