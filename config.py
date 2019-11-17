class Config:
    pass


class ProductionConfig(Config):
    DEBUG = False,
    ENV = 'Production'


class DevelopmentConfig(Config):
    DEBUG = True,
    ENV = 'Development',
    MONGO_URI = "mongodb://localhost:27017/protectu"


config = {
    'development': DevelopmentConfig,
}
