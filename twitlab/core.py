import os
import logging

from twitlab.globals import _get_logger

from configparser import ConfigParser
from flask import Flask
from sqlalchemy import create_engine

log = _get_logger(__name__)

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
    return config

def run(name):
    """ Starts a new server. """
    s = Flask(name)
    c = _load_config(s.root_path)
    log.debug('Default configuration loaded')   
    e, db = _init_engine(c, s)
    s.config.from_object(name)
    s.config.update(dict(
        DATABASE=c['database']['path']
        ,SECRET_KEY=c['database']['key']
        ,USERNAME=c['database']['user']
        ,PASSWORD=c['database']['passwd']
    ))
    s.config.from_envvar('FLASKR_SETTINGS', silent=True)
    log.debug('Flask application created')   
    return s, e

def _init_engine(config, app):
    """ Initializes the database engine. Opens a new connection to the
    database using a sqlalchemy engine. The path to the database is
    determined by checking the host parameter on the configuration. If the
    host is equal to '/' then it is assumed that the host is local and the
    rootpath is added to the full path. If not, the path will be the
    concatenation of the engine + host + path.
    
    Args: 

    - config A ConfigParser object that must have a database section
             with the subsections engine, path, host. It may also contain username and
             password. The 'path' member should be the relative path to the database
             if its stored locally.
    - app    A Flaks object
    
    returns a tuple e, p where e is the new engine and p is the full path to
    the database """
    c = config['database']
    path = c['engine']
    path += c['user']
    if c['passwd'] is not None and c['passwd'] is not '':
        path += ':' + c['passwd']
    if c['host'] is '/':
        if c['user'] is not None and c['user'] is not '':
            path += '@localhost'
        else:
            host = '/'
        path += os.path.join(app.root_path, '../', c['path'])
    else:
        path += c['path']
    log.debug('Database path: %s' % (path))   
    engine = create_engine(path)
    log.debug('Engine created')   
    return engine, path
