# -*- coding: utf-8 -*-
from . import Config

class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True

    SECRET_KEY = ''
    SQLALCHEMY_DATABASE_URI = ''

    SQLALCHEMY_BINDS = {
    }
