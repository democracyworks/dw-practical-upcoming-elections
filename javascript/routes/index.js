var express = require('express');
var router = express.Router();
var postalAbbreviations = require('../us_state.js');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Find My Election', states: postalAbbreviations });
});

module.exports = router;
