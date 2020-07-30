# Flask AFL API
A simple AFL (Australian Football League) themed REST API using Flask

This API utilises SQLAlchemy for an ORM with a PostgreSQL database and Pytest as a test framework.


## Getting Started

It is recommended that the user first creates a python virtual environment. The following command will install all dependencies including Flask related packages, SQLAlchemy, Pytest etc. 
``` $ pip3 install -r requirements.txt ```

### PostgreSQL
Some knowledge of PostgreSQL will be required as the reader will have to create two databases. PostgreSQL and a client, such as 'psql' will need to installed.

#### Create PostgresQL databases 
To create the main 'afl' database:
```
$ createdb afl
```

To create the test database (used for API tests):
```
$ createdb afl_test
```


### Flask
To initialise and/or update the database:
```
$ flask db init
$ flask db migrate
$ flask db upgrade
```

### app
The app itself is a package and will be installed along with other dependencies.
To use the development server, a couple of environment variables are required:
```
$ export FLASK_APP=app
$ export FLASK_ENV=development
```

Start the server:
```
$ flask run
```
Response should be something like:
```
$flask run
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
```


## The API
A user must login first in order to get an access token. Once logged in, the user will be able to obtain information regarding teams and players. For both team and player models, the user is able to perform CRUD operations. For most endpoints, the access token must be passed in as a header.
 
### API Endpoints
Assuming the development server is running, the URL for the API is ```http://127.0.0.1:5000/api/v1```

#### Create User
Creates a new user in the database

##### URL
/user/create

##### Method
POST

##### Params
{
    "username": <string>,
    "password": <string>
}

##### Success Response
Status Code: 201
Message: {"message": "user <username> has been created successfully."}


#### User Login
Log in user and obtain access token 

##### URL
/user/login

##### Method
POST

##### Params
{
    "username": <string>,
    "password": <string>
}

##### Success Response
Status Code: 200
Message: {"access_token": <token>}




#### Teams
Get all teams

##### URL
/teams

##### Method
GET

##### Headers
Content-Type: application/json
Authorization: Bearer <access_token>

##### Params
None

##### Success Response
Status Code: 200
Message: {"Count: <int>, "Teams": <[{Teams}]>

Example:
{
    "Count: 1, 
    "Teams": [
        {"id": 1,
        "location": "Melbourne",
        "name": "Essendon",
        "premierships": 12,
        "wooden_spoons": 7,
        "years_in_afl": 104
        }]
}


#### Team by ID
Get team by ID

##### URL
/team/<id>

##### Method
GET

##### Headers
Content-Type: application/json
Authorization: Bearer <access_token>

##### Params
id: <int>

##### Success Response
Status Code: 200
Message: {"message": "success", "team": <{Team}>}
