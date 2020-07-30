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
```$ createdb afl```

To create the test database (used for API tests):
```$ createdb afl_test```

To initialise and/or update the database:
```
$ flask db init
$ flask db migrate
$ flask db upgrade
```




