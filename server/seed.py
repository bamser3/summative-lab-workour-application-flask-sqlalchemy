#!/usr/bin/env python3

from app import app
from models import db, Exercise, Workout, WorkoutExercise
from datetime import date

with app.app_context():

    WorkoutExercise.query.delete()
    Exercise.query.delete()
    Workout.query.delete()

    db.session.commit()

    squat = Exercise(name="Squat", category="strength", equipment_needed=True)
    run = Exercise(name="Running", category="cardio", equipment_needed=False)
    plank = Exercise(name="Plank", category="strength", equipment_needed=False)

    db.session.add_all([squat, run, plank])
    db.session.commit()

    w1 = Workout(date=date.today(), duration_minutes=30, notes="Morning workout")
    w2 = Workout(date=date.today(), duration_minutes=45, notes="Evening workout")

    db.session.add_all([w1, w2])
    db.session.commit()

    we1 = WorkoutExercise(workout_id=w1.id, exercise_id=squat.id, reps=10, sets=3, duration_seconds=None)
    we2 = WorkoutExercise(workout_id=w1.id, exercise_id=plank.id, reps=None, sets=None, duration_seconds=60)
    we3 = WorkoutExercise(workout_id=w2.id, exercise_id=run.id, reps=None, sets=None, duration_seconds=900)

    db.session.add_all([we1, we2, we3])
    db.session.commit()

    print("Seeding complete")