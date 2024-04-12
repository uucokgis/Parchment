from pymongo.collection import Collection
from pymongo.errors import PyMongoError

from .client import db

parsomen_ayar_koleksiyonu: Collection = db['parsomen_ayar']


def parsomen_ayar_guncelle(parsomen_no: int, ayar):
    try:
        return parsomen_ayar_koleksiyonu.update_one({"parsomenNo": parsomen_no}, {"$set": {"ayar": ayar}})
    except PyMongoError as e:
        print(f"Error updating parsomen ayar: {e}")
        return None


def persomen_ayar_bul(parsomen_no: int):
    try:
        return parsomen_ayar_koleksiyonu.find_one({"parsomenNo": parsomen_no})
    except PyMongoError as e:
        print(f"Error finding parsomen ayar: {e}")
        return None
