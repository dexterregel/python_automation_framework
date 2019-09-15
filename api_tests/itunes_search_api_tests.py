
import requests
import json
from jsonpath import jsonpath

class iTunes_Search:

    def itunes_search_test(self):
        
        url = 'https://itunes.apple.com/search?term=awolnation'
        expected_status_code = 200

        response = requests.get(url)
        response_status_code = response.status_code
        response_json = json.loads(response.text)

        try:
            assert response_status_code == expected_status_code, ('Response status code of '
                + str(response_status_code) + ' did not match expected status code of '
                + str(expected_status_code))
        except Exception as err:
            print('itunes_search_test failed: ', err)

        results = jsonpath(response_json, 'results')

        for result in results[0]:
            print(jsonpath(result, 'trackName'))





test = iTunes_Search()
test.itunes_search_test()
        
