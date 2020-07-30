import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-key'
    DEBUG = False
    CSRF_ENABLED = True
    
class DevelopmentConfigDB(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/teams_api"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:adrian@localhost:5432/afl"
    DEBUG = True



class TestingConfigDB(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/teams_api"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:adrian@localhost:5432/afl_test"
    TESTING = True
    DEBUG = True
    

app_config = {
    'development': DevelopmentConfigDB,
    'testing': TestingConfigDB,
    }