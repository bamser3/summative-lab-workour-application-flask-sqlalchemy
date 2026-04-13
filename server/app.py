from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db
from flask import request, jsonify
from models import db, Workout, Exercise, WorkoutExercise

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/workouts', methods=['GET'])
def get_workouts():
    return jsonify({"message": "List all workouts"}), 200

@app.route('/workouts/<int:id>', methods=['GET'])
def get_workout(id):
    return jsonify({"message": f"Get workout {id}"}), 200

@app.route('/workouts', methods=['POST'])
def create_workout():
    return jsonify({"message": "Create workout"}), 201

@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    return jsonify({"message": f"Delete workout {id}"}), 200

@app.route('/exercises', methods=['GET'])
def get_exercises():
    return jsonify({"message": "List all exercises"}), 200

@app.route('/exercises/<int:id>', methods=['GET'])
def get_exercise(id):
    return jsonify({"message": f"Get exercise {id}"}), 200

@app.route('/exercises', methods=['POST'])
def create_exercise():
    return jsonify({"message": "Create exercise"}), 201

@app.route('/exercises/<int:id>', methods=['DELETE'])
def delete_exercise(id):
    return jsonify({"message": f"Delete exercise {id}"}), 200

@app.route('/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises', methods=['POST'])
def add_exercise_to_workout(workout_id, exercise_id):
    return jsonify({
        "message": f"Add exercise {exercise_id} to workout {workout_id}"
    }), 201