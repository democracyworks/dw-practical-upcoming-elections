""" This file contains the unit tests for querying data, collecting data
in a local repository, and ensuring that the length of the postal codes list == 61 and the states with current DemocracyWorks employees are in
the list """

# Library Imports
import unittest
import json

# Local Imports
from elections.us_states import postal_abbreviations
from elections.query import query_data, temp_store_data


class TestPostalAbbreviations(unittest.TestCase):
    """ Contains tests for postal_abbreviations list """

    def test_postal_abbreviations(self):
        # confirm that there are 61 postal abbreviations in us_states.py
        self.assertEqual(len(postal_abbreviations), 61)

        # confirm that all states with current DW employees are in the list of states
        dw_employee_states = ["CA", "CO", "DC", "IL",
                              "KS", "KY", "MN", "NY", "PA", "RI", "VA", "WA"]
        for state in dw_employee_states:
            self.assertIn(state, postal_abbreviations)


class TestQueryData(unittest.TestCase):
    """ Contains tests for querying data from Turbovote API """

    def test_query_data(self):
        json_test_object = [{'district-divisions': [{'ocd-id': 'ocd-division/country:us/state:fl/place:gainesville', 'voter-registration-authority-level': 'county', 'election-authority-level': 'county', 'voting-methods': [{'primary': False, 'start': '2019-03-09T00:00:00Z', 'type': 'early-voting', 'excuse-required': False, 'end': '2019-03-16T00:00:00Z'}, {'primary': True, 'instructions': {'voting-id': "You will be asked to show a valid photo ID with signature to vote in Florida. Acceptable forms include: Florida driver's license or ID card issued by the Department of Highway Safety and Motor Vehicles; US passport; debit or credit card; military ID; student ID; retirement center ID; neighborhood association ID; public assistance ID; veteran health ID; license to carry a concealed weapon or firearm; or an employee ID card issued by the federal government, the state of Florida, or any county or municipality. If your photo ID does not include your signature, you will be asked to provide another ID that has your signature.\n\nVoters without ID: If you are unable to provide ID, you will be able to vote a provisional ballot. Your ballot will count if the signature on your ballot matches the signature on your voter registration record."}, 'type': 'in-person', 'excuse-required': False}, {'primary': False, 'type': 'by-mail', 'excuse-required': False, 'ballot-request-deadline-received': '2019-03-12T00:00:00Z', 'acceptable-forms': [{'name': 'fl_absentee'}]}], 'voter-registration-methods': [{'deadline-postmarked': '2019-02-19T00:00:00Z', 'instructions': {'race': 'You are requested, but not required, to fill in this box.', 'idnumber': 'If you have one, you must provide your Florida driver\'s license number or Florida identification card number. If you do not have a Florida driver\'s license or identification card, you must provide the last four digits of your Social Security number. If you have not been issued any of these numbers, you must write the word "NONE".','signature': 'To register in Florida you must: \nbe a citizen of the United States \nbe a legal resident of both the State of Florida and of the county in which you seek to be registered \nbe 18 years old (you may pre-register if you are at least 16) \nnot be adjudicated mentally incapacitated with respect to voting in Florida or any other State, or if you have, you must first have your voting rights restored\nnot be a convicted felon, or if you are, you must first have your civil rights restored if they were taken away\nswear or affirm the following: "I will protect and defend the Constitution of the United States and the Constitution of the State of Florida, that I am qualified to register as an elector under the Constitution and laws of the State of Florida, and that all information in this application is true."'}, 'type': 'by-mail', 'acceptable-forms': [{'name': 'nvrf', 'fields': [{'race': 'requested'}]}]}, {'instructions': {'registration': "You should know: you need a Florida ID and a Social Security number to use Florida's online voter registration system. The name and address on the ID must match your voter registration exactly, so you should plan to have your ID on hand. If you don't have a Florida-issued ID, or don’t have your Florida-issued ID on hand, you can still register to vote by mail."}, 'type': 'online', 'supports-iframe': False, 'deadline-online': '2019-02-19T00:00:00Z', 'url': 'https://registertovoteflorida.gov/en/Registration/Eligibility'}]}], 'website': 'https://www.votealachua.com/Elections/Upcoming-Elections/2019-Gainesville-Regular', 'polling-place-url': 'https://registration.elections.myflorida.com/CheckVoterStatus', 'date': '2019-03-19T00:00:00Z', 'population': 132259, 'polling-place-url-shortened': 'https://tvote.org/2lZ6ONw', 'description': 'Gainesville Municipal Election', 'id': '5c5362f7-fe69-48ef-9586-7142d7bc83d2'}]
        
        self.assertEqual(query_data('gainesville', 'fl'), json_test_object)
        self.assertEqual(query_data('washington', 'dc'), [])
        self.assertEqual(query_data('brooklyn', 'ny'), [])


class TestTempStoreData(unittest.TestCase):
    """ Contains tests for temporarily storing data in dictionary """

    def test_temp_store_data(self):
        json_test_object = [{'district-divisions': [{'ocd-id': 'ocd-division/country:us/state:fl/place:gainesville', 'voter-registration-authority-level': 'county', 'election-authority-level': 'county', 'voting-methods': [{'primary': False, 'start': '2019-03-09T00:00:00Z', 'type': 'early-voting', 'excuse-required': False, 'end': '2019-03-16T00:00:00Z'}, {'primary': True, 'instructions': {'voting-id': "You will be asked to show a valid photo ID with signature to vote in Florida. Acceptable forms include: Florida driver's license or ID card issued by the Department of Highway Safety and Motor Vehicles; US passport; debit or credit card; military ID; student ID; retirement center ID; neighborhood association ID; public assistance ID; veteran health ID; license to carry a concealed weapon or firearm; or an employee ID card issued by the federal government, the state of Florida, or any county or municipality. If your photo ID does not include your signature, you will be asked to provide another ID that has your signature.\n\nVoters without ID: If you are unable to provide ID, you will be able to vote a provisional ballot. Your ballot will count if the signature on your ballot matches the signature on your voter registration record."}, 'type': 'in-person', 'excuse-required': False}, {'primary': False, 'type': 'by-mail', 'excuse-required': False, 'ballot-request-deadline-received': '2019-03-12T00:00:00Z', 'acceptable-forms': [{'name': 'fl_absentee'}]}], 'voter-registration-methods': [{'deadline-postmarked': '2019-02-19T00:00:00Z', 'instructions': {'race': 'You are requested, but not required, to fill in this box.', 'idnumber': 'If you have one, you must provide your Florida driver\'s license number or Florida identification card number. If you do not have a Florida driver\'s license or identification card, you must provide the last four digits of your Social Security number. If you have not been issued any of these numbers, you must write the word "NONE".','signature': 'To register in Florida you must: \nbe a citizen of the United States \nbe a legal resident of both the State of Florida and of the county in which you seek to be registered \nbe 18 years old (you may pre-register if you are at least 16) \nnot be adjudicated mentally incapacitated with respect to voting in Florida or any other State, or if you have, you must first have your voting rights restored\nnot be a convicted felon, or if you are, you must first have your civil rights restored if they were taken away\nswear or affirm the following: "I will protect and defend the Constitution of the United States and the Constitution of the State of Florida, that I am qualified to register as an elector under the Constitution and laws of the State of Florida, and that all information in this application is true."'}, 'type': 'by-mail', 'acceptable-forms': [{'name': 'nvrf', 'fields': [{'race': 'requested'}]}]}, {'instructions': {'registration': "You should know: you need a Florida ID and a Social Security number to use Florida's online voter registration system. The name and address on the ID must match your voter registration exactly, so you should plan to have your ID on hand. If you don't have a Florida-issued ID, or don’t have your Florida-issued ID on hand, you can still register to vote by mail."}, 'type': 'online', 'supports-iframe': False, 'deadline-online': '2019-02-19T00:00:00Z', 'url': 'https://registertovoteflorida.gov/en/Registration/Eligibility'}]}], 'website': 'https://www.votealachua.com/Elections/Upcoming-Elections/2019-Gainesville-Regular', 'polling-place-url': 'https://registration.elections.myflorida.com/CheckVoterStatus', 'date': '2019-03-19T00:00:00Z', 'population': 132259, 'polling-place-url-shortened': 'https://tvote.org/2lZ6ONw', 'description': 'Gainesville Municipal Election', 'id': '5c5362f7-fe69-48ef-9586-7142d7bc83d2'}]
        gainesville_dict = temp_store_data(json_test_object)

        self.assertEqual(gainesville_dict['description'], 'Gainesville Municipal Election')
        self.assertEqual(gainesville_dict['website'], 'https://www.votealachua.com/Elections/Upcoming-Elections/2019-Gainesville-Regular')
        self.assertTrue(gainesville_dict['early_voting'])
        self.assertTrue(gainesville_dict['by_mail'])
