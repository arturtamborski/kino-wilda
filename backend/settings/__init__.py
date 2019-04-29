import cklass
from pathlib import Path

from backend.settings.config import Config


cklass.load_config(Config)


BASE_DIR         = Path()


DEBUG            = Config.DEBUG
SECRET_KEY       = Config.SECRET_KEY
ALLOWED_HOSTS    = Config.ALLOWED_HOSTS


ROOT_URLCONF     = 'backend.urls'
WSGI_APPLICATION = 'backend.wsgi.application'


LANGUAGE_CODE    = 'en-us'
TIME_ZONE        = 'UTC'
USE_I18N         = True
USE_L10N         = True
USE_TZ           = True
STATIC_URL       = '/static/'


INSTALLED_APPS = (
    # django
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # plugins
    'rest_framework',

    # apps
    'backend.api',
)


MIDDLEWARE = (
    # django
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'local.sqlite3'),
    }
}
