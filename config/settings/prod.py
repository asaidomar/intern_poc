import pathlib

from .base import *

DEBUG = False

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = ["api.imaginhome.icade.fr",
                 "imaginhome.icade.fr",
                 "api.icade.lan", "icade.lan"]

INSTALLED_APPS = ['collectfast', ] + INSTALLED_APPS


"""
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader', ]
     ),
]

"""


# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DBNAME'),
        'USER': env('DBUSER'),
        'PASSWORD': env('DBPASSWORD'),
        'HOST': env('DBHOST'),
    }
}

#DATABASES['default']['ATOMIC_REQUESTS'] = True


MIDDLEWARE.insert(
    MIDDLEWARE.index('django.middleware.common.CommonMiddleware'),
    'corsheaders.middleware.CorsMiddleware'
)


# CACHING
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'imaginhome_cache_table',
    }
}

# CORS
CORS_ORIGIN_ALLOW_ALL = True

# Logging

LOG_LEVEL = env.str('LOG_LEVEL', default='INFO')
log_dir = pathlib.Path(__file__).parent.with_name("logs")
filename = log_dir.joinpath("api_box.log")


MEDIA_ROOT = "/srv/media"

CHECK_GOOGLE_RECAPTCHA = False
ACCOUNT_EMAIL_VERIFICATION = True

GOOGLE_RECAPTCHA_SECRET_KEY = '6LeRsXAUAAAAALhoc9o2_zwT4lI6Ub1dz-r9utec'

os.environ['wsgi.url_scheme'] = 'https'

MEDIA_URL = 'https://%s/media/' % FRONTEND_DOMAIN


ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = "http://" + FRONTEND_DOMAIN + "/login"
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = "http://" + FRONTEND_DOMAIN + "/login"