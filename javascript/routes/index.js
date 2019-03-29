var express = require('express');
var router = express.Router();
var us_states = require('../us_state.js');
var request = require('request');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Find My Election', states: us_states });
});

router.post('/search', function(req, res, next){
	/*assign contents of form req.body to variables*/
	const street1FromForm=req.body.street, zipFromForm=req.body.zip, cityFromForm=req.body.city, stateFromForm=req.body.state
	let URL=createURL(street1FromForm,cityFromForm,stateFromForm,zipFromForm)

	let electionResults= request.get(URL,(error,response,body)=>{
		console.log(body)
		return body
	})

	/*render views/results.hbs file*/
	res.render('results', {title:JSON.stringify(electionResults)});

});

/*-------------HELPER FUNCTIONS-----------*/
/* create URL is a function that takes all the form inputs and processes them using helper functions*/
function createURL(street1,city,state,zip){
	let stateAllLowerCase = state.toLowerCase()/*convert state to lower case using toLowerCase() method*/
	let cityNoSpaces=removeSpaces(city)
	let baseURL = 'https://api.turbovote.org/elections/upcoming?district-divisions='/*base URL which never changes*/
	let ocdid1 = `ocd-division/country:us/state:${stateAllLowerCase},`
	let ocdid2 = `ocd-division/country:us/state:${stateAllLowerCase}`
	let place = `/place:${cityNoSpaces}`
	let URL = baseURL+ocdid1+ocdid2+place
	return URL
}

/*this function will take a city and 1) remove all spaces 2) lower case*/
function removeSpaces(anyCity){
	let cityNoSpaces = anyCity.toLowerCase().replace(/ /g,'')
	/* find all spaces using a regular expression and remove them*/
	return cityNoSpaces
}


module.exports = router;
