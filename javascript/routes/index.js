var express = require('express');
var router = express.Router();
var us_states = require('../us_state.js');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Find My Election', states: us_states });
});

module.exports = router;
