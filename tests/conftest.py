import pytest

from mongomock import MongoClient

from pymongo import MongoClient as RealMongoClient

@pytest.fixture(scope='function')
def mongo_client(request):
    """Return a mongomock client"""
    _client = MongoClient()
    return _client