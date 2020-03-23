import os

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "rest_framework",
    "social_django",
    "rest_social_auth",
    "corsheaders",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]


SECRET_KEY = "STATICFILESECRETKEY"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
ENV = "staging" if os.environ.get("TRAVIS_BRANCH") == "staging" else "production"
print("Using env {}".format(ENV))
STATIC_URL = "/{}/static/".format(ENV)
