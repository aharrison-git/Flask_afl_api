from flask import request
from app import db
from app.model.players import PlayerModel
from flask import current_app as app


@app.route('/api/v1/players/search', methods=['GET','POST'])
def search_players():
    if request.method == 'POST':
        if request.is_json():
            data = request.get_json()
            players = PlayerModel.query
            if "first_name" in data: players = players.filter_by(first_name=data["first_name"])
            if "last_name" in data: players = players.filter_by(last_name=data["last_name"])
            if "dob" in data: players = players.filter_by(dob=data["dob"])
            if "matches_played" in data: players = players.filter_by(matches_played=data["matches_played"])
            if "career_goals" in data: players = players.filter_by(career_goals=data["career_goals"])

            players = players.all()
            results = [
                {
                "id": player.id,
                "first_name": player.frst_name,
                "last_name": player.last_name,
                "dob": player.dob,
                "matches_played": player.matches_played,
                "career_goals": player.career_goals,
                "team_id": player.team_id
            } for player in players]

            return {"count": len(players), "players": results}
        return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        players = PlayerModel.query
        if request.args.get("first_name"): players = players.filter_by(first_name=request.args.get("first_name"))
        if request.args.get("last_name"): players = players.filter_by(last_name=request.args.get("last_name"))
        if request.args.get("dob"): players = players.filter_by(dob=request.args.get("dob"))
        if request.args.get("matches_played"): players = players.filter_by(matches_played=request.args.get("matches_played"))
        if request.args.get("career_goals"): players = players.filter_by(career_goals=request.args.get("career_goals"))
        if request.args.get("team_id"): players = players.filter_by(team_id=request.args.get("team_id"))

        players = players.all()
        results = [
        {
            "id": player.id,
            "first_name": player.first_name,
            "last_name": player.last_name,
            "dob": player.dob,
            "matches_played": player.matches_played,
            "career_goals": player.career_goals,
            "team_id": player.team_id
        } for player in players]

        return {"count": len(players), "players": results}
        