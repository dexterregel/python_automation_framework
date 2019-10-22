
import requests
import json
from jsonpath import jsonpath


def test_itunes_search():
    
    url = 'https://itunes.apple.com/search'
    search_string_parameters = {
        'term': 'awolnation'
    }
    expected_status_code = 200
    expected_result = 'Sail'

    response = requests.get(url, params = search_string_parameters)
    response_status_code = response.status_code

    assert response_status_code == expected_status_code, ('Response status code of '
        + str(response_status_code) + ' did not match expected status code of '
        + str(expected_status_code))

    # change response data from a string in json format to a dict
    response_data = json.loads(response.text)

    results = jsonpath(response_data, 'results[*].trackName')

    try:
        assert expected_result in results, ('The expected result ' + expected_result
        + ' was not present in the results.')
    except Exception as err:
        print('itunes_search_test failed: ', err)
