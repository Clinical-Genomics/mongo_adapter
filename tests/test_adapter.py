from mongo_adapter import MongoAdapter

def test_setup(mongo_client):
    db_name = 'test'
    adapter = MongoAdapter(mongo_client)
    assert adapter.db is None
    
    adapter.setup(db_name)
    
    assert adapter.db == db_name