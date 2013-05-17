from settings_base import *

ENVIRONMENT = 'PROD'

ALLOWED_HOSTS = [
    'ohboss.herokuapp.com',
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

# Facebook Information
FACEBOOK_APP_ID = '322030074592338'
FACEBOOK_APP_SECRET = '12136999b94ef4c87acc17dd18e27480'

# AWS Information
AWS_ACCESS_KEY_ID = 'AKIAIWUXQY7UILQNXKDA'
AWS_SECRET_ACCESS_KEY = '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'
