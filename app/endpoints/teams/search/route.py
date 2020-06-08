from flask import request
from app import db
from app.model.teams import TeamModel
from flask import current_app as app
from flask_jwt_extended import jwt_required


@app.route('/api/v1/teams/search', methods=['POST', 'GET'])
@jwt_required
def search_teams():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            teams = TeamModel.query
            if "name" in data:
                teams = teams.filter_by(name=data["name"])
            if "premierships" in data:
                teams = teams.filter_by(premierships=data["premierships"])
            if "wooden_spoons" in data:
                teams = teams.filter_by(wooden_spoons=data["wooden_spoons"])
            if "years_in_afl" in data:
                teams = teams.filter_by(years_in_afl=data["years_in_afl"])
            if "location" in data:
                teams = teams.filter_by(location=data["location"])
            
            teams = teams.all()
            results = [
                {
                    "id": team.id,
                    "name": team.name,
                    "location": team.location,
                    "premierships": team.premierships,
                    "wooden_spoons": team.wooden_spoons,
                    "years_in_afl": team.years_in_afl
                } for team in teams]

            return {"count": len(results), "teams": results}
        return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        teams =TeamModel.query
        print("location: {}".format(request.args.get("location")))
        if request.args.get("name"):
            teams = teams.filter_by(name=request.args.get("name"))
        if request.args.get("location"):
            teams = teams.filter_by(location=request.args.get("location"))
        if request.args.get("premierships"):
            teams = teams.filter_by(premierships=request.args.get("premierships"))
        if request.args.get("wooden_spoons"):
            teams = teams.filter_by(wooden_spoons=request.args.get("wooden_spoons"))
        if request.args.get("years_in_afl"):
            teams = teams.filter_by(years_in_afl=request.args.get("years_in_afl"))

        teams = teams.all()
        results = [
            {
                "id": team.id,
                "name": team.name,
                "location": team.location,
                "premierships": team.premierships,
                "wooden_spoons": team.wooden_spoons,
                "years_in_afl": team.years_in_afl
            } for team in teams]

        return {"count": len(results), "teams": results}