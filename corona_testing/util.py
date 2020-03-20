import os
from .errors import EnvVariableNotSet


def required_env_var(var_name):
    var = os.environ.get(var_name)
    if var is None:
        raise EnvVariableNotSet(var_name)
    return var
