import pytest

import mongomock

from mongo_adapter import check_connection
from mongo_adapter import get_client

from pymongo.errors import InvalidURI

def test_check_connection(mongo_client):
    ## GIVEN a mongomock MongoClient
    
    ## WHEN checking if the connection works
    
    ## THEN assert that the connection is valid since it is a mock
    assert check_connection(mongo_client)

def test_get_connection():
    ## GIVEN a mongomock URI
    uri = "mongomock://"
    
    ## WHEN getting a client
    mock_client = get_client(uri=uri)
    
    ## THEN assert that the client is a mock client
    assert isinstance(mock_client, mongomock.MongoClient)
    ## THEN assert that the connection is valid since it is a mock
    assert check_connection(mock_client)

def test_get_client_wrong_uri():
    ## GIVEN a mongomock MongoClient
    
    ## WHEN checking if the connection works
    
    ## THEN assert that the connection is valid since it is a mock
    
    with pytest.raises(InvalidURI):
        get_client(uri="wierd uri")
