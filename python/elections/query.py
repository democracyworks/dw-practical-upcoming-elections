""" This file contains the function for querying data from the Turbovote API """

# Library Imports
import requests
import json


def query_data(city_name, state_abbreviation):
    """ Query the Turbovote API for local elections """

    query = 'https://api.turbovote.org/elections/upcoming?district-divisions=ocd-division/country:us/state:{0},ocd-division/country:us/state:{0}/place:{1}'.format(
        state_abbreviation, city_name)
    headers = {'Accept': 'application/json'}

    response = requests.get(query, headers=headers)
    json_response = response.json()
    return json_response
