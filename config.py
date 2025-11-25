import os

class Config(object):
    """Base configuration class."""
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        """Returns the database connection URL for the environment. Raises ValueError if DATABASE_URL environment variable is not set."""
        value = os.environ.get("DATABASE_URL")
        if not value:
            raise ValueError("DATABASE_URL is not set")
        return value

class DevelopmentConfig(Config):
    """Configuration for development environment."""
    DEBUG = True

class ProductionConfig(Config):
    """Configuration for production environment."""
    DEBUG = False

class TestingConfig(Config):
    """Configuration for testing environment."""
    TESTING = True
    
environment = os.environ.get("FLASK_ENV")
if environment == "production":
    app_config = ProductionConfig()
elif environment == "testing":
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()