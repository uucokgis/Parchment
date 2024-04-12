from pymongo.collection import Collection

from .hamur import hamur_koleksiyonu
from .parsomen import db, parsomen_koleksiyonu

blok_koleksiyonu: Collection = db['blok']


def yeni_blok(icerik_tipi: str, veri: str, sira_no: int, yer: int):
    """
    Yeni blok uretilir
    :param icerik_tipi: Raster | Metin
    :param veri: RasterUri | Metin
    :param sira_no:
    :param yer:
    :return:
    """
    return blok_koleksiyonu.insert({
        "icerik": {
            "tipi": icerik_tipi,
            "veri": veri,
        },
        "sira_no": sira_no,
        "yer": yer
    })


def blok_guncelle(blok_id, veri: str, sira_no: int, yer: int):
    return blok_koleksiyonu.update_one({"_id": blok_id},
                                       {"veri": veri,
                                        "sira_no": sira_no,
                                        "yer": yer}
                                       )


def blok_guncelle(parsomen_no: int, hamur_no: int, sira_no: int, **kwargs):
    return parsomen_koleksiyonu.update_one({"parsomen_no": parsomen_no, "hamur_no": hamur_no, sira_no: sira_no}, {
        **kwargs
    })


def blok_bul(parsomen_no: int, hamur_no: int, **kwargs):
    """

    :param parsomen_no: required
    :param hamur_no: required
    :param kwargs:
        min sira no, max sira no, pagination, sorting, limit
    :return:
    """
    # todo: think how to create relationships
    hamur = hamur_koleksiyonu.find_one(parsomen_no=parsomen_no, hamur_no=hamur_no)
    if not hamur:
        raise ValueError("Hamur not found!")

    bloklar = blok_koleksiyonu.find(f"""_id IN ${hamur.values()}""")
    return bloklar


def blok_getir(*blok_idler, **kwargs):
    """

    :param blok_idler:
    :param kwargs:
        pagination, sorting, limit, offset
    :return:
    """
    return blok_koleksiyonu.find({f"_id IN {blok_idler}"}, **kwargs)
