""" This file contains the function for querying data from the Turbovote API """

# Library Imports
import requests
import json


def query_data(city_name, state_abbreviation):
    """ Query the Turbovote API for local elections; return json if election data
    available else empty list """

    query = 'https://api.turbovote.org/elections/upcoming?district-divisions=ocd-division/country:us/state:{0},ocd-division/country:us/state:{0}/place:{1}'.format(
        state_abbreviation, city_name)
    headers = {'Accept': 'application/json'}

    response = requests.get(query, headers=headers)

    if response != []:
        json_response = response.json()
        return json_response
    else:
        return []


def temp_store_data(json_response):
    """ Temporarily store Turbovote API response data in dictionary """

    election_results_dict = {}

    election_results_dict['description'] = json_response[0]['description']
    election_results_dict['website'] = json_response[0]['website']
    election_results_dict['date'] = json_response[0]['date']
    election_results_dict['polling_place_url'] = json_response[0]['polling-place-url']
    election_results_dict['population'] = json_response[0]['population']
    election_results_dict['election_authority_level'] = json_response[0]['district-divisions'][0]['election-authority-level']
    election_results_dict['early_voting'] = True if json_response[0][
        'district-divisions'][0]['voting-methods'][0]['type'] == 'early-voting' else False
    election_results_dict['in_person'] = True if json_response[0][
        'district-divisions'][0]['voting-methods'][1]['type'] == 'in-person' else False
    election_results_dict['by_mail'] = True if json_response[0][
        'district-divisions'][0]['voting-methods'][2]['type'] == 'by-mail' else False

    return election_results_dict
