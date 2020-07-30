from app import db

class PlayerModel(db.Model):
    __tablename__ = 'player'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    dob = db.Column(db.Date(), nullable=True)
    matches_played = db.Column(db.Integer, nullable=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=True)
    career_goals = db.Column(db.Integer, nullable=True)

    team = db.relationship("TeamModel", backref="player")

    def __init__(self, first_name, last_name, dob, matches_played, team_id, career_goals):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.matches_played = matches_played
        self.team_id = team_id
        self.career_goals = career_goals

    def __repr__(self):
        return f"<Player {self.first_name} {self.last_name}>"