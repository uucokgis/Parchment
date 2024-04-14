from pymongo.collection import Collection

from parsomen.types.classes import Blok, Base
from .client import db
from ..helpers import construct_sira_no_filter


class BaseCollection:
    """
    Mainly two different operations: mutation and query
    mutation can be done with
        * Mutate document
        * Query document
    """
    collection: Collection
    base: Base

    def mutate(self, item: Base):  # create
        return self.collection.insert_one(item.__dict__)

    def mutate(self, _id, **item_props):  # update with id
        return self.collection.update_one({
            "_id": _id,
        }, {"$set": item_props}, upsert=True)

    def mutate(self, update_item: Base, **search_props):  # update with query
        return self.collection.update_one({**search_props}, {"$set": update_item}, upsert=True)

    def destroy(self, _id: str):
        return self.collection.delete_one({"_id": _id})

    def destroy(self, **search_props):
        return self.collection.delete_one(search_props)

    def query(self, return_one: bool, **search):
        if return_one:
            return self.collection.find_one(**search)
        else:
            return self.collection.find(**search)


class BlokCollection(BaseCollection):
    collection: Collection = db['blok']
    base: Blok

    def query(self, parsomen_no: int, hamur_no: int, min_sira_no=0, max_sira_no=-1):
        sira_no_filter = construct_sira_no_filter(min_sira_no, max_sira_no)
        return self.query(False, parsomen_no=parsomen_no, hamur_no=hamur_no, **sira_no_filter)


class HamurCollection(BaseCollection):
    pass


class ParsomenCollection(BaseCollection):
    pass


class ParsomenAyarCollection(BaseCollection):
    pass
