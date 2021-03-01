require 'test_helper'
require 'upcoming_elections/us_states'
include UsStates

class UsStatesTest < Minitest::Test
  def test_postal_abbreviations
    assert POSTAL_ABBREVIATIONS.count == 61
  end

  # confirm that all states with current DW employees are in the list of states
  def test_dw_employee_states_included
    dw_employee_states = %w[CA CO DC IL KS KY MN NY PA RI VA WA]
    dw_employee_states.each do |state|
      assert POSTAL_ABBREVIATIONS.include?(state)
    end
  end
end
