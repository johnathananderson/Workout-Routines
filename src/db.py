from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Workout(db.Model):
    __tablename__ = 'workout'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    main_muscle = db.Column(db.String, nullable = False)
    other_muscle = db.Column(db.String, nullable = False)
    workout_type = db.Column(db.String, nullable = False)
    mechanics = db.Column(db.String, nullable = False)
    equipment = db.Column(db.String, nullable = False)
    difficulty = db.Column(db.String, nullable = False)
    instructions = db.Column(db.String, nullable = False)
    picture_url = db.Column(db.String, nullable = False)

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.main_muscle = kwargs.get('main_muscle', '')
        self.other_muscle = kwargs.get('other_muscle', '')
        self.workout_type = kwargs.get('workout_type', '')
        self.mechanics = kwargs.get('mechanics', '')
        self.equipment = kwargs.get('equipment', '')
        self.difficulty = kwargs.get('difficulty', '')
        self.instructions = kwargs.get('instructions', '')
        self.picture_url = kwargs.get('picture_url', '')
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'main_muscle': self.main_muscle,
            'other_muscle': self.other_muscle,
            'workout_type': self.workout_type,
            'mechanics': self.mechanics,
            'equipment': self.equipment,
            'difficulty': self.difficulty,
            'instructions': self.instructions,
            'picture_url': self.picture_url
        }
