# Democracy Works Upcoming Elections Practical Exercise

Thank you for applying to work at Democracy Works! This coding exercise is
designed to show off your ability to program a small application that interacts
with an HTTP API. We know you are busy, so we ask that **you spend no more than
2 hours on the project** and then turn it in to us.

If you've previously applied to Democracy Works with this project, we ask that
you either 1) submit the work you completed previously, or 2) start your work
from scratch so that we can fairly judge your work against that of other
applicants.

## The project

You are building a web application that can tell people what elections they have
coming up based on their address. It is similar to the kinds of things you'd be
working on at Democracy Works and uses one of our APIs.

When someone visits the site you create, they will be presented with an address
form. When the user submits the form, your code will translate the address into
some OCD IDs (see below), query the Democracy Works Elections API for upcoming
elections for those OCD IDs, and display to the user any elections returned.

## Our grading rubric

We evaluate submissions according to the following criteria:

* The form submits
* State and place OCD IDs are correctly generated
* The Democracy Works Elections API is called correctly
* Returned elections are displayed to the user
* The results are formatted for the user
* The code that generates OCD IDs can be easily changed
* The project has documentation
* There are tests
* Functions/classes/methods are small and clearly scoped
* Names are clear

The goal is to see that you can get some working code that is readable to
others. We do not expect you to complete everything on this list, nor is this
list exhaustive of what would go into a "real" project (there is no
consideration for failure cases or deployment, for example).

## The anonymous review

In order to reduce potential bias, your submission will be graded anonymously.
To make that easier, please don't include any personally identifying information
in your code or documentation.

To avoid using your own address in documentation or tests, you can use
well-known places (like the White House or Disneyland) or the Democracy Works
office in Brooklyn (20 Jay St, Brooklyn, NY 11201).

## Project templates

Project templates exist for [Clojure][clojure-template],
[JavaScript][javascript-template], and [Python][python-template]. You may choose
another language, or choose to not work from these templates. If you choose to
not use a template, be sure to document how to run your project.

Pick a language that you're comfortable in. There are no bonus points for making
a particular choice here.

The templates include some libraries for HTTP routing and HTML templating. You
are encouraged to add dependencies as needed.

## About OCD IDs

OCD IDs are [Open Civic Data division identifiers][ocd-ids] and they look like
this (for the state of Massachusetts): `ocd-division/country:us/state:ma`

A given address can be associated with several OCD IDs. For example, an address
in Wayland, Massachusetts would be associated with the following OCD IDs:

* `ocd-division/country:us`
* `ocd-division/country:us/state:ma`
* `ocd-division/country:us/state:ma/cd:5`
* `ocd-division/country:us/state:ma/county:middlesex`
* `ocd-division/country:us/state:ma/place:wayland`
* `ocd-division/country:us/state:ma/sldl:13th_middlesex`
* `ocd-division/country:us/state:ma/sldu:norfolk_bristol_and_middlesex`

Not all of those are derivable from just the text of an address. For example,
merely having an address in Wayland doesn't tell us what county it is in; we
would have to query a system that understands how addresses relate to counties.

That said, we can derive a basic set of state and place (i.e. city) OCD IDs that
will be a good starting point for this project. This entails:

* creating the state OCD ID by lower-casing the state abbreviation and
  appending it to `ocd-division/country:us/state:`
* creating a copy of the state OCD ID
* appending `/place:` to it
* lower-casing the city value, replacing all spaces with underscores,
  and appending it to that

So, the city "Wayland" and the state "MA" would result in the OCD IDs:

* `ocd-division/country:us/state:ma`
* `ocd-division/country:us/state:ma/place:wayland`

Then you should supply both OCD IDs to your election API request, separated by a
comma as shown in the example URL below.

```
https://api.turbovote.org/elections/upcoming?district-divisions=ocd-division/country:us/state:ma,ocd-division/country:us/state:ma/place:wayland
```

## About the API

The upcoming elections API endpoint lives at
`https://api.turbovote.org/elections/upcoming`. You'll make `GET` requests to
it.

You'll need to supply a query string with a `district-divisions` key. Its value
should be comma-delimited OCD IDs. See the example above.

The response will be in the [EDN format][edn] (commonly used in Clojure) by
default, but you can request JSON by setting your request's Accept header to
`application/json` if you prefer.

The API is not configured to allow all origins for [CORS][cors], so you won't be
able to make requests directly from a browser. You'll have to have a server
process to make those requests. The provided templates have you covered.

## Current elections

Depending on the time of year and whether it's an odd or even-numbered year, the
number of elections in the system can vary wildly. We maintain an [up-to-date
list of OCD IDs that will return an election][upcoming-elections] until the
dates they are listed under. Please refer to that for example OCD IDs that will
return an election to your app.

[ocd-ids]: http://opencivicdata.readthedocs.io/en/latest/data/datatypes.html
[edn]: https://github.com/edn-format/edn
[upcoming-elections]: https://github.com/democracyworks/dw-practical-upcoming-elections/wiki/Upcoming-Elections
[cors]: https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS

[clojure-template]: https://github.com/democracyworks/dw-practical-upcoming-elections/tree/master/clojure
[javascript-template]: https://github.com/democracyworks/dw-practical-upcoming-elections/tree/master/javascript
[python-template]: https://github.com/democracyworks/dw-practical-upcoming-elections/tree/master/python
