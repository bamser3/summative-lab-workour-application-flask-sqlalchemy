from marshmallow import Schema, fields, validates, ValidationError, post_load
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import Exercise, Workout, WorkoutExercise

class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    equipment_needed = fields.Bool()

    @validates("name")
    def validate_name(self, value):
        if not value or len(value.strip()) < 2:
            raise ValidationError("Name must be at least 2 characters")

    @validates("category")
    def validate_category(self, value):
        allowed = ["strength", "cardio", "flexibility", "balance"]
        if value not in allowed:
            raise ValidationError(f"Category must be one of {allowed}")

    @post_load
    def make_exercise(self, data, **kwargs):
        return Exercise(**data)
    
class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    duration_minutes = fields.Int(required=True)
    notes = fields.Str()

    @validates("duration_minutes")
    def validate_duration(self, value):
        if value is None or value <= 0:
            raise ValidationError("Duration must be greater than 0")

    @post_load
    def make_workout(self, data, **kwargs):
        return Workout(**data)
    
    
class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    workout_id = fields.Int(required=True)
    exercise_id = fields.Int(required=True)
    reps = fields.Int(allow_none=True)
    sets = fields.Int(allow_none=True)
    duration_seconds = fields.Int(allow_none=True)

    @validates("reps")
    def validate_reps(self, value):
        if value is not None and value < 1:
            raise ValidationError("Reps must be at least 1")

    @validates("sets")
    def validate_sets(self, value):
        if value is not None and value < 1:
            raise ValidationError("Sets must be at least 1")

    @post_load
    def make_workout_exercise(self, data, **kwargs):
        return WorkoutExercise(**data)