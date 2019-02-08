"""Configuration file"""
import os


class Config:
    """Parent configuration class."""
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    """Configurations for the development environment"""
    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing"""
    TESTING = True
    DEBUG = True


class StagingConfig(Config):
    """Configurations for a staging environment"""
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for a production environment"""
    DEBUG = False
    TESTING = False
