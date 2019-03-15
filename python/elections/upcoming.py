import functools
import requests
import json

from elections.us_states import postal_abbreviations

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('address_form', __name__, url_prefix='/')


@bp.route('/', methods=('GET', 'POST'))
def search():
    if request.method == 'POST':
        redirect(url_for('search'))

    return render_template('address_form.html', states=postal_abbreviations)


@bp.route('/search', methods=('POST',))
def fetch_elections():
    if request.method == 'POST':
        city_name = str(request.form['city']).lower().replace(' ', '_')
        state_abbrev = str(request.form['state']).lower()

        json_reponse = query_data(city_name, state_abbrev)
        return render_template('upcoming_elections.html', city=city_name, state=state_abbrev, results=json_reponse)


def query_data(city_name, state_abbreviation):
    """ Query the Turbovote API for local elections """
    state_ocd_id = 'ocd-division/country:us/state:'+state_abbreviation
    city_ocd_id = state_ocd_id+'/place:'+city_name
    query_url = 'https://api.turbovote.org/elections/upcoming?district-divisions='

    query = query_url+state_ocd_id+','+city_ocd_id
    headers = {'accept': 'application/json'}

    response = requests.get(
        query, headers=headers)
    data = response.json()
    return data
