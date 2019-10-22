
import requests
import json
from jsonpath import jsonpath


def test_search_store_locations():

    url = 'https://www.marcos.com/api/stores/searchByStreetAddress'
    query_string_parameters = {
        'orderType': 'Delivery',
        'radius': '5',
        'addressType': 'Single Family',
        'street': '867 Woodbury Road',
        'city': 'Orlando',
        'state': 'FL',
        'zip': '32828',
        'country': 'US'
    }
    expected_status_code = 200
    expected_result = 'Orlando - #8050'

    response = requests.get(url, params = query_string_parameters)

    assert response.status_code == expected_status_code, ('Response status'
        ' code of ' + str(response.status_code) + ' did not matched the'
        ' expected status code of ' + str(expected_status_code))

    response_data = json.loads(response.text)

    result = jsonpath(response_data, 'results[0].id')

    assert result[0] == expected_result, ('Result ' + result[0]
        + ' did not match the expected result ' + expected_result)
