from mongo_adapter import MongoAdapter

def test_setup(mongo_client):
    db_name = 'test'
    adapter = MongoAdapter(mongo_client)
    assert adapter.db is None
    
    adapter.setup(db_name)
    
    assert adapter.db_name == db_name

def test_setup_flask(flask_app):
    db_name = flask_app.config['MONGO_DBNAME']
    
    adapter = MongoAdapter()
    
    adapter.init_app(flask_app)
    
    assert adapter.db_name == db_name

def test_init_with_dbname(mongo_client):
    db_name = 'test'
    adapter = MongoAdapter(mongo_client, db_name)
    
    assert adapter.db_name == db_name
