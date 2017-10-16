# -*- coding: utf-8 -*-
from . import Config

class TestingConfig(Config):

    SECRET_KEY = ''
    SQLALCHEMY_DATABASE_URI = ''
    SQLALCHEMY_BINDS = {
    }
