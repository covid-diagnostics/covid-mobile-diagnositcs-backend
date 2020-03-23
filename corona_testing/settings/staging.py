# import sentry_sdk
# from sentry_sdk.integrations.django import DjangoIntegration

from corona_testing.settings.base import *

# SENTRY_DSN = required_env_var("SENTRY_DSN")

# sentry_sdk.init(dsn=SENTRY_DSN, integrations=[DjangoIntegration()])

# MIDDLEWARE.extend(["whitenoise.middleware.WhiteNoiseMiddleware"])
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEBUG = False
STORAGE_URL = "https://staging-storage-corona-testing.s3-eu-west-1.amazonaws.com/"
STATIC_URL = STORAGE_URL + "static/"
MEDIA_URL = STORAGE_URL + "media/"

AWS_STORAGE_BUCKET_NAME = "staging-storage-corona-testing"
# AWS_QUERYSTRING_AUTH = False
# AWS_S3_CUSTOM_DOMAIN = "staging.static.corona_testing.io"


DEFAULT_FILE_STORAGE = "corona_testing.settings.storages.PublicMediaStorage"
STATICFILES_STORAGE = "corona_testing.settings.storages.StaticStorage"

# HOSTNAME="https://staging.api.corona_testing.io"
