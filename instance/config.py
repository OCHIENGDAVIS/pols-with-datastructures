import os
"""Configuration file"""
import os


class Config:
    """Parent configuration class."""
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY")


class DevelopmentConfig(Config):
    """Configurations for the development environment"""
    DEBUG = True
    DEVELOPMENT = True
    DB_USER = os.environ.get("DB_USER")
    DB_HOST = os.environ.get("DB_HOST")
    DB = os.environ.get("DB_NAME")
    DB_PASSWORD = os.environ.get("DB_PASSWORD")



class TestingConfig(Config):
    """Configurations for Testing"""
    TESTING = True
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for a production environment"""
    DEBUG = False
    TESTING = False
