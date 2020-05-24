from flask import request
from app import db
from app.model.players import PlayerModel
from app import Helpers
from flask import current_app as app

@app.route('/api/v1/players', methods=['POST', 'GET'])
def handle_players():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_player = PlayerModel(
                first_name = data['first_name'],
                last_name = data['last_name'],
                dob = data['dob'],
                matches_played = data['matches_played'],
                career_goals = data['career_goals'],
                team_id = data['team_id']
            )
            db.session.add(new_player)
            db.session.commit()
            return {"message": f"player {new_player.first_name} {new_player.last_name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        players = PlayerModel.query.all()
        results = [
            {
                "id": player.id,
                "first_name": player.first_name,
                "last_name": player.last_name,
                "dob": Helpers.convertDateObjToDateString(player.dob),
                "matches_played": player.matches_played,
                "career_goals": player.career_goals,
                "team_id": player.team_id
            }
        for player in players]
        return {"count": len(players), "players": results}