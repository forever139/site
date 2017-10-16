# coding: UTF-8
import os

def load_config(mode=os.getenv('FLASK_CONFIG')):
    """Load config."""
    try:
        if mode == 'production':
            from .production import ProductionConfig
            return ProductionConfig
        elif mode == 'testing':
            from .test import TestingConfig
            return TestingConfig
        else:
            from .development import DevelopmentConfig
            return DevelopmentConfig
    except ImportError:
        from .development import DevelopmentConfig
        return DevelopmentConfig

class Config(object):
    """
    Common configurations
    """
    # Put any configurations here that are common across all environments
