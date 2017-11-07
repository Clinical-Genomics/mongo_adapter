import pytest

from mongomock import MongoClient

from pymongo import MongoClient as RealMongoClient

class MockFlaskApp(object):
    """Mock a Flask App"""
    def __init__(self, host='localhost', port=27017, db_name='test'):
        client = MongoClient()
        
        self.config = {}
        self.extensions = {'pymongo': {}}
        

        self.config['MONGO_DBNAME'] = db_name
        self.config['MONGO_PORT'] = port
        self.config['MONGO_HOST'] = host
        
        self.extensions['pymongo']['MONGO'] = ['', client[db_name]]

@pytest.fixture(scope='function')
def mongo_client(request):
    """Return a mongomock client"""
    _client = MongoClient()
    return _client

@pytest.fixture(scope='function')
def flask_app(request):
    _mock = MockFlaskApp()
    return _mock

