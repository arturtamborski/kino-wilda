class Config:

    # public
    DEBUG = False

    PRODUCTION = False

    SECRET_KEY = ''
    API_KEY = ''

    ALLOWED_HOSTS = ['localhost', '127.0.0.1']

    # private
    omdb_url = 'http://www.omdbapi.com/'
