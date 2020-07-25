from flask import request, jsonify
from app import db
from app.model.users import UsersModel
from flask import current_app as app
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

from werkzeug.security import check_password_hash, generate_password_hash


@app.route('/api/v1/user', methods=['GET'])
@jwt_required
def handle_get_user():
    current_user = get_jwt_identity()
    return jsonify({"logged in as": current_user}), 200


@app.route('/api/v1/user/create', methods=['POST'])
def handle_create_user():
    if request.is_json:
        data = request.get_json()
        user_exists = UsersModel.query.filter_by(username=data["username"])
        print("user exists: {}".format(user_exists))
        print("user exists all: {}".format(user_exists.all()))
        if len(user_exists.all()) == 0:
            new_user = UsersModel(username=data["username"])
            new_user.set_password(data["password"])
            db.session.add(new_user)
            db.session.commit()
            return {"message": f"user {new_user.username} has been created successfully."}, 201
        else:
            return {"message": f"user already exists"}
    else:
        return {"error": "The request payload is not in JSON format"}



if __name__ == "__main__":
    user = UsersModel(username='Ima_user')
    user.set_password("test1234")
    db.session.add(user)
    db.session.commit()
    q = UsersModel.query.filter_by(username="Ima_user")
    print(f"q username: {username}")
    print(f"q password: {q.password}")
    print("check: {}".format(user.check_password("test1234")))
    