from elections.us_states import postal_abbreviations

def test_postal_abbreviations():
    # confirm that there are 61 postal abbreviations in us_states.py
    assert len(postal_abbreviations) == 61

    # confirm that all states with current DW employees are in the list of states
    dw_employee_states = ["AR", "CA", "CO", "DC", "IL", "MN", "NY", "OR", "RI", "TN", "VA", "WA"]
    for state in dw_employee_states:
        assert state in postal_abbreviations
