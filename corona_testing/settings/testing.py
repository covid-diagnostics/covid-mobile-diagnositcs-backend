from corona_testing.settings.development import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "corona_testing_test",
        "USER": "postgres",
        "PASSWORD": "",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}