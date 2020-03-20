"""Small util functions used throught the app"""
import os


def get_canonical_postcode(postcode):
    short = postcode.replace(" ", "")
    return "{} {}".format(short[:-3], short[-3:])


def get_base_url():
    """Returns the base frontend url for this env without a trailing slash"""
    env: str = os.environ.get("DJANGO_SETTINGS_MODULE")
    env_name = env.split(".")[-1]

    if env_name == "production":
        return "https://app.corona_testing.io"
    elif env_name == "staging":
        return "https://staging.app.corona_testing.io"

    return "http://localhost:3000"
