import requests

from backend import settings


def fetch_movie_from_omdb(title):
    params = {
        'apikey': settings.Config.API_KEY,
        't': title,
        'type': 'movie',
    }

    r = requests.get(settings.Config.omdb_url, params=params)
    json = r.json()

    if r.status_code != 200:
        return {'Response': 'False', 'Error': f'Status code r.status_code'}

    return json
