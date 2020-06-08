from flask import request, jsonify
from app import db
from app.model.users import UsersModel
from flask import current_app as app
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required


@app.route('/api/v1/user', methods=['GET'])
@jwt_required
def handle_get_user():
    current_user = get_jwt_identity()
    return jsonify({"logged in as": current_user}), 200


@app.route('/api/v1/user/create', methods=['POST'])
def handle_create_user():
    if request.is_json:
        data = request.get_json()
        new_user = UsersModel(username=data["username"], password=data["password"])
        db.session.add(new_user)
        db.session.commit()
        return {"message": f"user {new_user.username} has been created successfully."}
    else:
        return {"error": "The request payload is not in JSON format"}