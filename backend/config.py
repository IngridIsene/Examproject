  

# configuration class
class Config(object):
  DATABASE = 'database.db'
  DATABASE_URL="sqlite:///database.db"

class ProductionConfig(Config):
  DEBUG=False

class DevelopmentConfig(Config):
  DEBUG=True