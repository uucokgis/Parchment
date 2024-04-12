from graphene import ObjectType, Int, List, Schema, ID

from parsomen.db.hamur import hamur_koleksiyonu
from parsomen.semalar.blok import BlokSema


class Hamur(ObjectType):
    """
     _id: ObjectId
    parsomenId: number
    bloklar: number []  # Blok id'leri sirali gelecek
    sira: number
    # (1)
    """
    _id = ID()
    parsomenNo = Int(description="Parsomen ID")
    bloklar = List(Int, description="Doğru sırayla Blok id'leri")
    siraNo = Int(description="Sıra numarası")

    def resolve_hamur(self, hamur_id):
        return hamur_koleksiyonu.find_one({"_id": hamur_id})

    def resolve_hamur(self, parsomen_no, sira_no):
        return hamur_koleksiyonu.find_one({"parsomenNo": parsomen_no, "siraNo": sira_no})


hamur_sema = Schema(query=Hamur)
