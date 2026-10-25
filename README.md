# Workout API

A RESTful API built with Flask, SQLAlchemy, and Marshmallow for managing workouts and exercises.

## Features

- Retrieve all workouts and individual workouts.
- Create and delete workouts.
- Retrieve all exercises and individual exercises.
- Create and delete exercises.
- Add exercises to workouts.
- Validate incoming data and handle errors.
- Enforce database constraints and relationships.
- Seed the database with sample workout data.

## Technologies Used

- Python 3.8
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLAlchemy
- Marshmallow
- SQLite

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/nyabokechantel83-dev/work-api.git
cd work-api
```

### 2. Install dependencies

Make sure Python 3.8 and Pipenv are installed.

```bash
pipenv install
```

### 3. Set up the database

```bash
pipenv run flask --app server.app db upgrade
```

### 4. Seed the database

```bash
pipenv run python -m server.seed
```

### 5. Start the server

```bash
pipenv run flask --app server.app run --port 5555
```

The API will be available at `http://127.0.0.1:5555`.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/workouts` | Get all workouts |
| GET | `/workouts/<workout_id>` | Get one workout |
| POST | `/workouts` | Create a workout |
| DELETE | `/workouts/<workout_id>` | Delete a workout |
| GET | `/exercises` | Get all exercises |
| GET | `/exercises/<exercise_id>` | Get one exercise |
| POST | `/exercises` | Create an exercise |
| DELETE | `/exercises/<exercise_id>` | Delete an exercise |
| POST | `/workouts/<workout_id>/exercises/<exercise_id>/workout_exercises` | Add an exercise to a workout |

## Example Requests

Create a workout:

```json
{
  "date": "2026-10-27",
  "duration_minutes": 40,
  "notes": "Leg day"
}
```

Create an exercise:

```json
{
  "name": "Lunges",
  "category": "Strength",
  "equipment_needed": false
}
```

Add an exercise to a workout:

```json
{
  "sets": 3,
  "reps": 12
}
```

## Error Handling

The API returns appropriate HTTP status codes for successful requests, invalid data, missing resources, and database constraint violations.

## License

This project was created for educational purposes.
