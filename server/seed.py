
from datetime import date

from server.app import app
from server.models import db, Exercise, Workout, WorkoutExercise


with app.app_context():
    db.session.query(WorkoutExercise).delete()
    db.session.query(Workout).delete()
    db.session.query(Exercise).delete()
    db.session.commit()

    squat = Exercise(
        name="Squats",
        category="Strength",
        equipment_needed=False
    )

    push_up = Exercise(
        name="Push-ups",
        category="Strength",
        equipment_needed=False
    )

    treadmill = Exercise(
        name="Treadmill Running",
        category="Cardio",
        equipment_needed=True
    )

    workout_one = Workout(
        date=date(2026, 10, 25),
        duration_minutes=45,
        notes="Full body training"
    )

    workout_two = Workout(
        date=date(2026, 10, 26),
        duration_minutes=30,
        notes="Cardio session"
    )

    db.session.add_all([
        squat,
        push_up,
        treadmill,
        workout_one,
        workout_two
    ])

    db.session.flush()

    db.session.add_all([
        WorkoutExercise(
            workout=workout_one,
            exercise=squat,
            sets=3,
            reps=12
        ),
        WorkoutExercise(
            workout=workout_one,
            exercise=push_up,
            sets=3,
            reps=10
        ),
        WorkoutExercise(
            workout=workout_two,
            exercise=treadmill,
            duration_seconds=1200
        )
    ])

    db.session.commit()

    print("Database seeded successfully!")
