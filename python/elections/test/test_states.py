""" This file contains the unit tests for querying data, collecting data
in a local repository, and ensuring that the length of the postal codes list == 61 and the states with current DemocracyWorks employees are in
the list """

# Library Imports
import unittest

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
