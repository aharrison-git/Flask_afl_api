from flask import request, jsonify
from app import db
from app.model.users import UsersModel
from flask import current_app as app
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
import logging

LOGGER = logging.getLogger(__name__)



@app.route('/api/v1/user/login', methods=['POST'])
def handle_login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)

    user_db = UsersModel.query.filter_by(username=username).first()

    if not username:
        return jsonify({"message": "Missing username parameter"}), 400
    if not password:
        return jsonify({"message": "Missing password parameter"}), 400
    if user_db is None:
        return jsonify({"message": "Bad username or password"}), 401
    if username != user_db.username or user_db.check_password(password) == False:
        LOGGER.debug("user route username -  db: {}, request: {}".format(user_db.username, username))
        LOGGER.debug("user route password -  db: {}, request: {}".format(user_db.check_password(password), password))
        return jsonify({"message": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify({"access_token": access_token}), 200


