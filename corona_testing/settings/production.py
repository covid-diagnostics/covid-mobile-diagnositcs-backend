from corona_testing.settings.base import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

SENTRY_DSN = required_env_var("SENTRY_DSN")

sentry_sdk.init(dsn=SENTRY_DSN, integrations=[DjangoIntegration()])

MIDDLEWARE.extend(["whitenoise.middleware.WhiteNoiseMiddleware"])
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


DEBUG = False
STORAGE_URL = "https://production.static.corona_testing.io/"
STATIC_URL = STORAGE_URL + "static/"
MEDIA_URL = STORAGE_URL + "media/"

AWS_STORAGE_BUCKET_NAME = "production.corona_testing-storage"
AWS_QUERYSTRING_AUTH = False
AWS_S3_CUSTOM_DOMAIN = "production.static.corona_testing.io"


DEFAULT_FILE_STORAGE = "corona_testing.settings.storages.PublicMediaStorage"
STATICFILES_STORAGE = "corona_testing.settings.storages.StaticStorage"
