
from marshmallow import Schema, fields, validate, validates_schema, ValidationError


class ExerciseSummarySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    category = fields.Str()
    equipment_needed = fields.Bool()


class WorkoutSummarySchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date()
    duration_minutes = fields.Int()
    notes = fields.Str(allow_none=True)


class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    workout_id = fields.Int(dump_only=True)
    exercise_id = fields.Int(dump_only=True)
    reps = fields.Int(allow_none=True)
    sets = fields.Int(allow_none=True)
    duration_seconds = fields.Int(allow_none=True)
    exercise = fields.Nested(ExerciseSummarySchema, dump_only=True)


class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)

    name = fields.Str(
        required=True,
        validate=validate.Length(min=1, max=100, error="Name is required and must be at most 100 characters"),
    )

    category = fields.Str(
        required=True,
        validate=validate.Length(min=1, max=50, error="Category is required and must be at most 50 characters"),
    )

    equipment_needed = fields.Bool(required=True)

    workouts = fields.Nested(
        WorkoutSummarySchema,
        many=True,
        dump_only=True
    )


class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)

    date = fields.Date(required=True)

    duration_minutes = fields.Int(
        required=True,
        strict=True,
        validate=validate.Range(min=1, error="Duration must be positive")
    )

    notes = fields.Str(allow_none=True)

    workout_exercises = fields.Nested(
        WorkoutExerciseSchema,
        many=True,
        dump_only=True
    )


class WorkoutExerciseInputSchema(Schema):
    reps = fields.Int(
        load_default=None,
        strict=True,
        allow_none=True,
        validate=validate.Range(min=1)
    )

    sets = fields.Int(
        load_default=None,
        strict=True,
        allow_none=True,
        validate=validate.Range(min=1)
    )

    duration_seconds = fields.Int(
        load_default=None,
        strict=True,
        allow_none=True,
        validate=validate.Range(min=1)
    )

    @validates_schema
    def validate_exercise_details(self, data, **kwargs):
        if not any(
            data.get(key) is not None
            for key in ("reps", "sets", "duration_seconds")
        ):
            raise ValidationError(
                "Provide at least one of reps, sets, or duration_seconds."
            )
