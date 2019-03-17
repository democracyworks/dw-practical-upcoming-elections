""" This file contains the blueprint and routes for identifying local elections
based on the user's entered city and state """

# Library Imports
import functools
import requests
import json

# Local Imports
from elections.us_states import postal_abbreviations
from elections.query import query_data
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('address_form', __name__, url_prefix='/')

# Route for gathering data from user
@bp.route('/', methods=('GET', 'POST'))
def search():
    if request.method == 'POST':
        redirect(url_for('search'))

    return render_template('address_form.html', states=postal_abbreviations)

# Route for querying and presenting election results to user
@bp.route('/search', methods=('POST',))
def fetch_elections():
    if request.method == 'POST':
        city_name = str(request.form['city']).lower().replace(' ', '_')
        state_abbreviation = str(request.form['state']).lower()

        json_reponse = query_data(city_name, state_abbreviation)
        return render_template('upcoming_elections.html', city=city_name, state=state_abbreviation, results=json_reponse)
