# Workout Tracker API

## Description

This is a Flask backend API for a workout tracking application. It
allows users to create workouts, create exercises, and link exercises to
workouts with sets, reps, or duration.

------------------------------------------------------------------------

## Installation

1.  Clone the repo:

```bash
git clone https://github.com/bamser3/summative-lab-workout-application-flask-sqlalchemy.git`
```
Then:
```bash
cd summative-lab-workout-application-flask-sqlalchemy
```
2.  Install dependencies:
```bash
pipenv install
```

```bash
pipenv shell
```

3.  Set up the database:
```bash
cd server flask db init flask db migrate -m "initial migration"
```
Then:
```bash
flask db upgrade
```


4.  Seed the database:
```bash
python seed.py
```

------------------------------------------------------------------------

## Run Instructions
```bash
cd server
```

From the `server` folder:

```bash

flask --app app run --port 5555 --debug
```
------------------------------------------------------------------------

## Endpoints

### Workouts

-   GET /workouts\
    Get all workouts

-   GET /workouts/`<id>`{=html}\
    Get a single workout

-   POST /workouts\
    Create a workout

-   DELETE /workouts/`<id>`{=html}\
    Delete a workout

------------------------------------------------------------------------

### Exercises

-   GET /exercises\
    Get all exercises

-   GET /exercises/`<id>`{=html}\
    Get a single exercise

-   POST /exercises\
    Create an exercise

-   DELETE /exercises/`<id>`{=html}\
    Delete an exercise

------------------------------------------------------------------------

### WorkoutExercises (Join Table)

-   POST
    /workouts/`<workout_id>`{=html}/exercises/`<exercise_id>`{=html}/workout_exercises\
    Add an exercise to a workout with reps, sets, or duration

------------------------------------------------------------------------

## Pipfile Dependencies

```bash
[packages]
flask = "3.1.3"
flask-sqlalchemy = "3.1.1"
flask-migrate = "4.1.0"
marshmallow = "4.3.0"
flask-marshmallow = "1.4.0"
marshmallow-sqlalchemy = "1.5.0"

[requires]
python_version = "3.12.3"
```

------------------------------------------------------------------------

## Tests

No formal test files included. Endpoints were tested using postman, browser,
Flask shell, and manual requests.
