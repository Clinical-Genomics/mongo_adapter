from mongo_adapter import check_connection

def test_check_connection(mongo_client):
    ## GIVEN a mongomock MongoClient
    
    ## WHEN checking if the connection works
    
    ## THEN assert that the connection is valid since it is a mock
    assert check_connection(mongo_client)