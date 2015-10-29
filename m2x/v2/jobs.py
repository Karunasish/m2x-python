from m2x.v2.resource import Resource

class Job(Resource):
    COLLECTION_PATH = 'jobs'
    ITEM_PATH = 'jobs/{id}'
    ITEMS_KEY = 'jobs'
