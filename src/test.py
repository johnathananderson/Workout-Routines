import unittest
import json
import requests

LOCAL_URL = 'http://localhost:5000'
BODY = {'name': 'Push-Up', 'main_muscle': 'Chest', 'other_muscle': 'Triceps', 'workout_type': 'Test type', 'mechanics': 'Test mechanics', 'equipment': 'N/A', 'difficulty': 'Beginner', 'instructions': 'Test instructions', 'picture_url': 'Test picture url'}

class TestRoutes(unittest.TestCase):

    
    # # Tests getting all workouts
    # def test_get_initial_workouts(self):
    #     res = requests.get(LOCAL_URL + '/api/workouts/')
    #     assert res.json()['success']
    
    def test_create_database(self):
        requests.post(LOCAL_URL + '/api/workout/create/')

    # Tests creating a workout
    # def test_create_workout(self):
    #     res = requests.post(LOCAL_URL + '/api/workouts/', data=json.dumps(BODY))
    #     workout = res.json()['data']
    #     assert res.json()['success']
    #     assert workout['name'] == 'Push-Up'
    #     assert workout['main_muscle'] == 'Chest'
    #     assert workout['other_muscle'] == 'Triceps'
    #     assert workout['workout_type'] == 'Test type'
    #     assert workout['mechanics'] == 'Test mechanics'
    #     assert workout['equipment'] == 'N/A'
    #     assert workout['difficulty'] == 'Beginner'
    #     assert workout['instructions'] == 'Test instructions'
    #     assert workout['picture_url'] == 'Test picture url'

    # # Tests getting a workout by id
    # def test_get_workout(self):
    #     res = requests.post(LOCAL_URL + '/api/workouts/', data=json.dumps(BODY))
    #     workout = res.json()['data']

    #     res = requests.get(LOCAL_URL + '/api/workout/' + str(workout['id']) + '/')
    #     assert res.json()['data'] == workout

    # # Tests updating a workout
    # def test_edit_workout(self):
    #     res = requests.post(LOCAL_URL + '/api/workouts/', data=json.dumps(BODY))
    #     workout_id = res.json()['data']['id']
    #     res = requests.post(LOCAL_URL + '/api/workout/' + str(workout_id) + '/',
    #                         data=json.dumps({'name': 'New name'}))
    #     assert res.json()['success']

    #     res = requests.get(LOCAL_URL + '/api/workout/' + str(workout_id) + '/')
    #     assert res.json()['data']['name'] == 'New name'

    # # Tests deleting a workout
    # def test_delete_workout(self):
    #     res = requests.post(LOCAL_URL + '/api/workouts/', data=json.dumps(BODY))
    #     workout_id = res.json()['data']['id']
    #     res = requests.delete(LOCAL_URL + '/api/workout/' + str(workout_id) + '/')
    #     assert res.json()['success']

    # # Tests getting a workout that doesn't exist
    # def test_get_invalid_workout(self):
    #     res = requests.get(LOCAL_URL + '/api/workout/1000/')
    #     assert not res.json()['success']

    # # Tests editing a workout that doesn't exist
    # def test_edit_invalid_workout(self):
    #     res = requests.post(LOCAL_URL + '/api/workout/1000/',
    #                         data=json.dumps({'name': 'New name'}))
    #     assert not res.json()['success']

    # # Tests deleting a workout that doesn't exist
    # def test_delete_invalid_workout(self):
    #     res = requests.delete(LOCAL_URL + '/api/workout/1000/')
    #     assert not res.json()['success']

    # # Tests to make sure that the workout id increments
    # def test_workout_id_increments(self):
    #     res = requests.post(LOCAL_URL + '/api/workouts/', data=json.dumps(BODY))
    #     workout_id = res.json()['data']['id']

    #     res2 = requests.post(LOCAL_URL + '/api/workouts/', data=json.dumps(BODY))
    #     workout_id2 = res2.json()['data']['id']

    #     assert workout_id + 1 == workout_id2

if __name__ == '__main__':
    unittest.main()
