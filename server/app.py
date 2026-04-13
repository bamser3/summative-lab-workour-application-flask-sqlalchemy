from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Workout, Exercise, WorkoutExercise
from schemas import WorkoutSchema, ExerciseSchema, WorkoutExerciseSchema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)

workout_exercise_schema = WorkoutExerciseSchema()


@app.route('/workouts', methods=['GET'])
def get_workouts():
    workouts = Workout.query.all()
    return jsonify(workouts_schema.dump(workouts)), 200


@app.route('/workouts/<int:id>', methods=['GET'])
def get_workout(id):
    workout = Workout.query.get_or_404(id)
    return jsonify(workout_schema.dump(workout)), 200


@app.route('/workouts', methods=['POST'])
def create_workout():
    data = request.get_json()
    workout = workout_schema.load(data)

    db.session.add(workout)
    db.session.commit()

    return jsonify(workout_schema.dump(workout)), 201


@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    workout = Workout.query.get_or_404(id)

    db.session.delete(workout)
    db.session.commit()

    return jsonify({"message": "Workout deleted"}), 200


@app.route('/exercises', methods=['GET'])
def get_exercises():
    exercises = Exercise.query.all()
    return jsonify(exercises_schema.dump(exercises)), 200


@app.route('/exercises/<int:id>', methods=['GET'])
def get_exercise(id):
    exercise = Exercise.query.get_or_404(id)
    return jsonify(exercise_schema.dump(exercise)), 200


@app.route('/exercises', methods=['POST'])
def create_exercise():
    data = request.get_json()
    exercise = exercise_schema.load(data)

    db.session.add(exercise)
    db.session.commit()

    return jsonify(exercise_schema.dump(exercise)), 201


@app.route('/exercises/<int:id>', methods=['DELETE'])
def delete_exercise(id):
    exercise = Exercise.query.get_or_404(id)

    db.session.delete(exercise)
    db.session.commit()

    return jsonify({"message": "Exercise deleted"}), 200


@app.route('/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises', methods=['POST'])
def add_exercise_to_workout(workout_id, exercise_id):
    data = request.get_json()

    workout_exercise = WorkoutExercise(
        workout_id=workout_id,
        exercise_id=exercise_id,
        reps=data.get("reps"),
        sets=data.get("sets"),
        duration_seconds=data.get("duration_seconds")
    )

    db.session.add(workout_exercise)
    db.session.commit()

    return jsonify(workout_exercise_schema.dump(workout_exercise)), 201


if __name__ == "__main__":
    app.run(port=5555, debug=True)