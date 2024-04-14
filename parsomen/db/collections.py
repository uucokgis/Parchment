from pymongo.collection import Collection

from parsomen.types.classes import Base, Hamur, Parsomen, ParsomenAyar
from .client import db


class BaseCollection:
    """
        * Mutate document
            - Create new
            - Update
            - Update or create
        * Query document
            - Find (singular)
            - Search (plural)
    """
    collection: Collection
    base: Base

    @classmethod
    def create(cls, item: Base):  # create
        return cls.collection.insert_one(item.__dict__)

    @classmethod
    def update(cls, _id, **item_props):  # update with id
        return cls.collection.update_one({
            "_id": _id,
        }, {"$set": item_props}, upsert=True)

    @classmethod
    def update_with_query(cls, update_item: Base, **search_props):  # update with query
        return cls.collection.update_one({**search_props}, {"$set": update_item}, upsert=True)

    @classmethod
    def destroy_by_id(cls, _id: str):
        return cls.collection.delete_one({"_id": _id})

    @classmethod
    def destroy_by_query(cls, **search_props):
        return cls.collection.delete_one(search_props)

    @classmethod
    def query(cls, return_one: bool, **search):
        if return_one:
            return cls.collection.find_one(search)
        else:
            return cls.collection.find(search)


class HamurCollection(BaseCollection):
    collection: Collection = db['hamur']
    base: Hamur


class ParsomenCollection(BaseCollection):
    collection = db['parsomen']
    base = Parsomen


class ParsomenAyarCollection(BaseCollection):
    collection = db['parsomen_ayar']
    base = ParsomenAyar


class BlokCollection(BaseCollection):
    collection: Collection = db['blok']
    base: Blok

    @classmethod
    def query_with_hierarchy(cls, parsomen_no: int, hamur_no: int, min_sira_no=0, max_sira_no=-1):
        sira_no_filter = construct_sira_no_filter(min_sira_no, max_sira_no)
        return cls.query(False, parsomenNo=parsomen_no, hamurNo=hamur_no, **sira_no_filter)

