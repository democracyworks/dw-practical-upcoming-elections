var tap = require('tap');
var postal_abbreviations = require('../us_state.js');

const employee_states = ["CA", "CO", "DC", "IL", "KS", "KY",
                         "MN", "NY", "RI", "VA", "WA"];

tap.equal(postal_abbreviations.length, 61,
          'there are 61 states, territories, military abbreviations, etc.');

employee_states.forEach(abbr => {
  tap.assert(postal_abbreviations.includes(abbr),
             `postal_abbreviations contains ${abbr}`);
});
