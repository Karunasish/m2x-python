from m2x.v2.resource import Resource

class Collection(Resource):
    COLLECTION_PATH = 'collections'
    ITEM_PATH = 'collections/{id}'
    ITEMS_KEY = 'collections'
