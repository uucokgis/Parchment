from pymongo.collection import Collection

from .client import db

hamur_koleksiyonu: Collection = db['hamur']


def hamur_getir(parsomen_no: int, sira_no: int):
    return hamur_koleksiyonu.find_one({"parsomenNo": parsomen_no, "siraNo": sira_no})


def hamurlari_bul(parsomen_no: int, min_sira_no=1, max_sira_no=-1):
    return hamur_koleksiyonu.find({"parsomenNo": parsomen_no})
