class Config:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:password@localhost/ownerspets'


class DevConfig(Config):
    DEBUG = True
