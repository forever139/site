# -*- coding: utf-8 -*-
from . import Config

class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False
    SECRET_KEY = ''
    SQLALCHEMY_DATABASE_URI = ''
    SQLALCHEMY_BINDS = {
    }
