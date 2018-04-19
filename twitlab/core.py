import os

from configparser import ConfigParser
from flask import Flask

def _load_config(path):
    """ Loads the main configuration file.
        This file loads the main configuration file with path
        "./config.ini".

        It must contain the following sections:
        * database
          * user - username used for database connection
          * passwd - username's database
          * path - path to the database
          * key -

        returns config Dict
    """
    config = ConfigParser()
    config.read(os.path.join(path, '../devconfig.ini'))
    print(config.sections())
    return config

def run(name):
    """ Starts a new server. """
    s = Flask(name)
    c = _load_config(s.root_path)
    s.config.from_object(name)
    s.config.update(dict(
        DATABASE=os.path.join(s.root_path, '../', c['database']['path'])
        ,SECRET_KEY=c['database']['key']
        ,USERNAME=c['database']['user']
        ,PASSWORD=c['database']['passwd']
    ))
    s.config.from_envvar('FLASKR_SETTINGS', silent=True)
    return s