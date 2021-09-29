#!/usr/bin/env python3

"""Generates a markdown file containing OCD IDs for upcoming elections, grouped
by election date and sorted by OCD ID."""

import json
import itertools
import os
import urllib.request

def extract_data(x):
    """Returns a dict with "date" and "ocd_id" keys pulled out of an election
    data structure as returned by the TurboVote API."""
    return { 'date': x['date'][0:10],
             'ocd_id': x['district-divisions'][0]['ocd-id'] }

def sort_by_date(it):
    """Sort iterable of dicts in "it" by an expected "date" key."""
    return sorted(it, key=lambda x: x['date'])

def group_by_date(it):
    """Group pre-sorted iterable of dicts in "it" by an expected "date" key."""
    return itertools.groupby(it, lambda x: x['date'])

def fetch_api_data(url, api_key):
    """Returns full response from the TurboVote API."""
    r = urllib.request.Request(url)
    r.add_header("Accept", "application/json")
    r.add_header("Authorization", f"apikey {api_key}")
    with urllib.request.urlopen(r) as f:
        return f.read().decode('utf-8')

if __name__ == "__main__":
    api_key = os.environ.get('API_KEY')
    api_url = 'https://api.turbovote.org/elections/upcoming'

    json_data = json.loads(fetch_api_data(api_url, api_key))

    print("""# OCD IDs for upcoming elections by date

Each header in this document groups OCD IDs by the date of the election for
which each OCD ID will return a valid result from the TurboVote API.

You can use the OCD IDs in your testing as you work through the practical.

**Note:** this document is automatically generated, and the elections contained
within may be out of date.""")

    for k, vals in group_by_date(sort_by_date(map(extract_data, json_data))):
        print(f"\n## {k}\n")
        for v in sorted([v['ocd_id'] for v in vals]):
            print(f"- `{v}`")
