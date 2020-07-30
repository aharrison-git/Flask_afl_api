from flask import request
from app import db
from app.model.teams import TeamModel
from flask import current_app as app
from flask_jwt_extended import jwt_required
import logging


LOGGER = logging.getLogger(__name__)

@app.route('/api/v1/teams', methods=['POST', 'GET'])
@jwt_required
def handle_teams():
    print("request method: {}".format(request.method))
    #LOGGER.debug("teams handler")
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_team = TeamModel(name=data['name'], 
                                    location=data['location'], 
                                    premierships=data['premierships'], 
                                    wooden_spoons=data['wooden_spoons'], 
                                    years_in_afl=data['years_in_afl'])
            db.session.add(new_team)
            db.session.commit()
            return {"message": f"Team {new_team.name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        teams =TeamModel.query.all()
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