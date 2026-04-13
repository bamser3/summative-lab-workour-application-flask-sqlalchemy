from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Exercise(db.Model):
    __tablename__ = 'exercises'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    category = db.Column(db.String)
    equipment_needed = db.Column(db.Boolean)
    
    workout_exercises = db.relationship('WorkoutExercise', back_populates='exercise', cascade='all, delete-orphan')
    
    @validates('name')
    def validate_name(self, key, value):
        if not value or len(value) < 2:
            raise ValueError("Exercise names should be longer than 2 letters.")
        return value

class Workout(db.Model):
    __tablename__ = 'workouts'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    duration_minutes = db.Column(db.Integer)
    notes = db.Column(db.String)
    
    workout_exercises = db.relationship('WorkoutExercise', back_populates='workout', cascade='all, delete-orphan')
    
    @validates('duration_minutes')
    def validate_minutes(self, key, value):
        if not value or value < 0:
            raise ValueError("Exercises duration must be greater than 0")

class WorkoutExercise(db.Model):
    __tablename__ = 'workout_exercises'

    id = db.Column(db.Integer, primary_key=True)

    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    duration_seconds = db.Column(db.Integer)

    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))

    workout = db.relationship(
        'Workout',
        back_populates='workout_exercises'
    )

    exercise = db.relationship(
        'Exercise',
        back_populates='workout_exercises'
    )

    @validates('reps')
    def validate_reps(self, key, value):
        if value is not None and value < 1:
            raise ValueError("Reps must be at least 1 if provided")
        return value

    @validates('sets')
    def validate_sets(self, key, value):
        if value is not None and value < 1:
            raise ValueError("Sets must be at least 1 if provided")
        return value
