import requests
import json
from jsonpath import jsonpath
import random


class reqres_api_tests:

    def get_user(self):

        url = 'https://reqres.in/api/users'
        expected_status_code = 200

        # send the request and get the response
        response = requests.get(url)

        assert response.status_code == expected_status_code, ('Response status code of '
            + str(response.status_code) + ' did not match expected status code of '
            + str(expected_status_code))

        response_json = json.loads(response.text)

        total_data = len(jsonpath(response_json, 'data')[0])
        per_page = jsonpath(response_json, 'per_page')[0]


    def post_user(self):

        url = 'https://reqres.in/api/users'
        expected_status_code = 201
        #request_json = json.load(open('C:\\Users\\Dexter\\Programming\\Python\\Automation_take2\\POM\\api_tests\\request_jsons\\reqres_post_user.json', mode='r'))
        request_json = json.loads(json.dumps({"name": "another name", "job": "another job"}))
        # get the expected values from the request json
        expected_name = jsonpath(request_json, 'name')[0]
        expected_job = jsonpath(request_json, 'job')[0]

        # send the post request and get the response
        response = requests.post(url, request_json)

        assert response.status_code == expected_status_code, ('Response status code of '
            + str(response.status_code) + ' did not match expected status code of '
            + str(expected_status_code))

        response_json = json.loads(response.text)

        response_name = jsonpath(response_json, 'name')[0]
        response_job = jsonpath(response_json, 'job')[0]
        response_id = jsonpath(response_json, 'id')[0]
        response_createdAt = jsonpath(response_json, 'createdAt')[0]

        # verify the response contained the expected results
        assert response_name == expected_name, ('The response name ' + response_name
            + ' did not match the expected name ' + expected_name)
        assert response_job == expected_job, ('The response job ' + response_job
            + ' did not match the expected job ' + expected_job)
        assert response_id is not None, 'A response ID was not returned.'
        assert response_createdAt is not None, 'A user creation time was not returned.'


    def put_user(self):
        
        url = 'https://reqres.in/api/users'
        expected_status_code = 200
        # load json file
        request_json = json.load(open('C:\\Users\\Dexter\\Programming\\Python\\Automation_take2\\POM\\api_tests\\request_jsons\\reqres_put_user.json', mode='r'))
        # get the expected values from the request json
        expected_name = jsonpath(request_json, 'name')
        expected_job = jsonpath(request_json, 'job')

        # send the request and get the response
        response = requests.put(url, request_json)

        assert response.status_code == expected_status_code, ('Response status code of '
            + str(response.status_code) + ' did not match expected status code of '
            + str(expected_status_code))

        response_json = json.loads(response.text)

        response_name = jsonpath(response_json, 'name')
        response_job = jsonpath(response_json, 'job')
        response_updatedAt = jsonpath(response_json, 'updatedAt')

        assert response_name == expected_name, ('The response name ' + response_name
            + ' did not match the expected name ' + expected_name)
        assert response_job == expected_job, ('The response job ' + response_job
            + ' did not match the expected job ' + expected_job)
        assert response_updatedAt is not None, 'An update time was not returned.'

test = reqres_api_tests()
test.put_user()

