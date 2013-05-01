from settings_base import *

ENVIRONMENT = 'PROD'

ALLOWED_HOSTS = [
    'ohboss.herokuapp.com',
    'ohboss.com',
    'www.ohboss.com',
]

DEBUG = False
TEMPLATE_DEBUG = DEBUG
DAJAXICE_DEBUG = DEBUG

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'ohboss'
AWS_S3_FILE_OVERWRITE = True
AWS_QUERYSTRING_AUTH = False
AWS_HEADERS = {
    'Cache-Control': 'public, max-age=%s' % (30 * 24 * 60 * 60),
}
COMPRESS_STORAGE = STATICFILES_STORAGE

STATIC_URL = 'https://s3.amazonaws.com/ohboss/'
MEDIA_URL = 'https://s3.amazonaws.com/ohboss/'

# Set your DSN value
RAVEN_CONFIG = {
    'dsn': 'https://72751d7b7a174ea8932d0e6fb8f1e192:e17a9554929d4f92b966bbb4c0023e3c@app.getsentry.com/6931',
}
