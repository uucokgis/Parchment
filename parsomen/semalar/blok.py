from datetime import datetime

from graphene import ObjectType, String, Int, Field, DateTime, ID

from parsomen.db.blok import blok_koleksiyonu


class Icerik(ObjectType):
    tipi = String(required=True)
    data = String(required=True)


class BlokSema(ObjectType):
    """
        _id: ObjectId
    icerik: {tipi: String, data: String}
    sira: Number
    yer: Number

    # hepsinde olmalı (1)
    uretilmeTarihi: timestamp
    duzenlenmeTarihi: timestamp

    """
    _id = ID(required=True)
    icerik = Field(Icerik, required=True)
    sira = Int(required=True)
    yer = Int(required=True)
    uretilmeTarihi = DateTime(default_value=datetime.now())
    duzenlenmeTarihi = DateTime(default_value=datetime.now())

    @staticmethod
    def blok_getir(blok_id):
        return blok_koleksiyonu.find_one({'_id': blok_id})

    @staticmethod
    def blok_getir(parsomen_no, hamur_no, min_sira_no, max_sira_no):
        return blok_koleksiyonu.find({
            "parsomenNo": parsomen_no,
            "hamurNo": hamur_no,
            "sira_no_ge": min_sira_no,
            "sira_no_le": max_sira_no
        })
