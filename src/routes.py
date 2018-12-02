import json
from db import db, Workout
from flask import Flask, request

db_filename = "workout.db"
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % db_filename
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
with app.app_context():
    db.create_all()

@app.route("/")
@app.route("/api/workouts/")
def get_workouts():
  workouts = Workout.query.all()
  result = {'success': True, 'data': [workout.serialize() for workout in workouts]}
  return json.dumps(result), 200

@app.route("/api/workouts/<string:workout_body_part>/")
def get_workouts_by_part(workout_body_part):
  workouts = Workout.query.filter_by(body_part=workout_body_part).all()
  if workouts is not None:
    return json.dumps({'success': True, 'data': [workout.serialize() for workout in workouts]}), 200
  return json.dumps({'success': False, 'error': "Exercises not found!"}), 404

@app.route("/api/workouts/", methods=['POST'])
def create_workout():
  workout_body = json.loads(request.data)

  workout = Workout(
    name = workout_body.get('name'),
    main_muscle = workout_body.get('main_muscle'),
    other_muscle = workout_body.get('other_muscle'),
    workout_type = workout_body.get('workout_type'),
    mechanics = workout_body.get('mechanics'),
    equipment = workout_body.get('equipment'),
    difficulty = workout_body.get('difficulty'),
    instructions = workout_body.get('instructions'),
    picture_url = workout_body.get('picture_url'),
  )

  db.session.add(workout)
  db.session.commit()
  return json.dumps({'success': True, 'data': workout.serialize()}), 201

@app.route("/api/workout/<int:workout_id>/")
def get_workout(workout_id):
  workout = Workout.query.filter_by(id=workout_id).first()
  if workout is not None:
    return json.dumps({'success': True, 'data': workout.serialize()}), 200
  return json.dumps({'success': False, 'error': "Workout not found!"}), 404

@app.route("/api/workout/<int:workout_id>/", methods=['POST'])
def edit_workout(workout_id):
  workout = Workout.query.filter_by(id=workout_id).first()
  if workout is not None:
    workout_body = json.loads(request.data)
    workout.name = workout_body.get('name', workout.name)
    workout.main_muscle = workout_body.get('main_muscle', workout.main_muscle)
    workout.other_muscle = workout_body.get('other_muscle', workout.other_muscle)
    workout.workout_type = workout_body.get('workout_type', workout.workout_type)
    workout.mechanics = workout_body.get('mechanics', workout.mechanics)
    workout.equipment = workout_body.get('equipment', workout.equipment)
    workout.difficulty = workout_body.get('difficulty', workout.difficulty)
    workout.instructions = workout_body.get('instructions', workout.instructions)
    workout.picture_url = workout_body.get('picture_url', workout.picture_url)
    db.session.commit()
    return json.dumps({'success': True, 'data': workout.serialize()}), 200
  return json.dumps({'success': False, 'error': "Workout not found!"}), 404

@app.route("/api/workout/<int:workout_id>/", methods=['DELETE'])
def delete_workout(workout_id):
  workout = Workout.query.filter_by(id=workout_id).first()
  if workout is not None:
    db.session.delete(workout)
    db.session.commit()
    return json.dumps({'success': True, 'data': workout.serialize()}), 200
  return json.dumps({'success': False, 'error': "Workout not found!"}), 404

@app.route("/api/workout/create/", methods=['POST'])
def load_database():
    workouts = json.load(open('output.json'))
    workout_list = []
    for x in range(1299):
        workout = Workout(
            name = workouts[x][0],
            main_muscle = workouts[x][1],
            other_muscle = workouts[x][2],
            workout_type = workouts[x][3],
            mechanics = workouts[x][4],
            equipment = workouts[x][5],
            difficulty = workouts[x][6],
            instructions = workouts[x][7],
            picture_url = workouts[x][8]
        )
        workout_list.append(workout)
        db.session.add(workout)
        db.session.commit()
    return json.dumps({'success': True, 'data': [workout.serialize() for workout in workout_list]}), 201
    

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)  
