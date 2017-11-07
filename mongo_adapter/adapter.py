import logging

LOG = logging.getLogger(__name__)

class MongoAdapter(object):
    """Adapter for communicating with a mongo database"""
    def __init__(self, client, database=None):
        self.client = client
        self.db = None
        if database:
            self.setup(database)
    
    def init_app(self, app):
        """Setup via Flask"""
        host = app.config.get('MONGO_HOST', 'localhost')
        port = app.config.get('MONGO_PORT', 27017)
        dbname = app.config['MONGO_DBNAME']
        log.info("connecting to database: %s:%s/%s", host, port, dbname)
        self.setup(app.extensions['pymongo']['MONGO'][1])
        
    
    def setup(self, database):
        """Setup connection to a database"""
        self.db = self.client[database]
        # Specify collections that will be used here when overriding
        # eg self.food_collection = self.db.food etc
    
    def __str__(self):
        return "MongoAdapter(db={0})".format(self.db)