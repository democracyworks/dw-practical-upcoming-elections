import functools

from elections.us_states import postal_abbreviations

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
# from werkzeug.security import check_password_hash, generate_password_hash

# from flaskr.db import get_db

bp = Blueprint('address_form', __name__, url_prefix='/')


@bp.route('/', methods=('GET', 'POST'))
def search():
    """Take in an address."""
    if request.method == 'POST':
        address1 = request.form['street']
        address2 = request.form['street-2']
        city = request.form['city']
        state = request.form['state']
        zip = request.form['zip']
        return render_template('election_results.html')

    return render_template('address_form.html', states=states)
