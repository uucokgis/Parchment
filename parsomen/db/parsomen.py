from pymongo.collection import Collection

from .client import db

parsomen_koleksiyonu: Collection = db['parsomen']


def parsomen_ara(**kwargs):
    return parsomen_koleksiyonu.find(kwargs)


def yeni_parsomen(baslik: str, hamurlar, ayar):
    """

    :param baslik:
    :param hamurlar: Liste şeklinde Hamur şemaları
    :param ayar: AyarSema
    :return: OK
    """
    return parsomen_koleksiyonu.insert_one({
        "baslik": baslik,
        "hamurlar": hamurlar,
        "ayar": ayar
    })


def parsomen_guncelle(parsomen_id: int, **kwargs):
    """
    Parsomen bulunur
    :param kwargs: Parsomen fields
    :param parsomen_id:
    :return:
    """

    return parsomen_koleksiyonu.update_one(
        {"_id": parsomen_id},
        {"$set": kwargs}  # burada **kwargs kullanıyorum.
    )