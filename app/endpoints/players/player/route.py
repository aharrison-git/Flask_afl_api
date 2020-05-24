from flask import request
from app import db
from flask import current_app as app
from app.model.players import PlayerModel
import datetime
from app import Helpers

@app.route('/api/v1/players/<player_id>', methods=['GET','PUT','PATCH', 'DELETE'])
def handle_player(player_id):
    player = PlayerModel.query.get_or_404(player_id)
    if request.method == 'GET':
        response = {
            "player_id": player.id,
            "first_name": player.first_name,
            "last_name": player.last_name,
            "dob": Helpers.convertDateObjToDateString(player.dob),
            "matches_played": player.matches_played,
            "career_goals": player.career_goals,
            "team": {
                "id": player.team.id,
                "name": player.team.name
            }
        }
        return {"message": "success", "player": response}

    elif request.method == 'PUT':
        data = request.get_json()
        player.first_name = data['first_name']
        player.last_name = data['last_name']
        player.dob = data['dob']
        player.matches_played = data['matches_played']
        player.career_goals = data['career_goals']
        player.team_id = data['team_id']
        db.session.add(player)
        db.session.commit()
        return { "message": f"Player {player.first_name} {player.last_name} successfully updated"}

    elif request.method == 'PATCH':
        data = request.get_json()
        if 'first_name' in data: player.first_name = data['first_name']
        if 'last_name' in data: player.last_name = data['last_name']
        if 'dob' in data: player.dob = data['dob']
        if 'matches_played' in data: player.matches_played = data['matches_played']
        if 'career_goals' in data: player.career_goals = data['career_goals']
        if 'team_id' in data: player.team_id = data['team_id']
        db.session.add(player)
        db.session.commit()
        return { "mesage": f"Player {player.first_name} {player.last_name} successfully updated"}

    elif request.method == 'DELETE':
        db.session.delete(player)
        db.session.commit()
        return { "message": f"Player {player.first_name} {player.last_name} successfully deleted"}