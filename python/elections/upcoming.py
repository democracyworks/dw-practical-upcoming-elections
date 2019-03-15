import functools

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
def do_something():
    if request.method == 'POST':
        city_name = str(request.form['city'])
        state_name = str(request.form['state'])
        return render_template('upcoming_elections.html', city=city_name, state=state_name)
