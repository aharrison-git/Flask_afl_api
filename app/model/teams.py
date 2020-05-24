from app import db

class TeamModel(db.Model):
    __tablename__ = 'team'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    location = db.Column(db.String(20))
    premierships = db.Column(db.Integer)
    wooden_spoons = db.Column(db.Integer)
    years_in_afl = db.Column(db.Integer)

    def __init__(self, name, location, premierships, wooden_spoons, years_in_afl):
        self.name = name
        self.location = location
        self.premierships = premierships
        self.wooden_spoons = wooden_spoons
        self.years_in_afl = years_in_afl

    def __repr__(self):
        return f"<Team {self.name}>"