from graphene import ObjectType, Field, Int, Schema, List

from parsomen.db.blok import blok_getir, blok_bul
from parsomen.db.hamur import hamur_getir
from parsomen.semalar.blok import BlokSema
from parsomen.semalar.hamur import Hamur
from parsomen.semalar.parsomen_ayar import ParsomenAyar


class Query(ObjectType):
    parsomen_ayar = Field(ParsomenAyar, parsomen_no=Int(required=True))

    hamur = Field(Hamur, parsomen_no=Int(required=True), sira_no=Int(required=True))

    bloklar = List(BlokSema, parsomen_no=Int(required=True), hamur_no=Int(required=True),
                   min_sira=Int(required=False),
                   max_sira=Int(required=False))

    def resolve_parsomen_ayar(self, info, parsomen_no):
        ayar = ParsomenAyar.ayar_getir(parsomen_no)
        return ayar

    def resolve_hamur(self, info, parsomen_no, sira_no):
        data = hamur_getir(parsomen_no, sira_no)
        return Hamur(**data)

    # def resolve_hamur(self, info, parsomen_no, min_sira_no, max_sira_no):
    #     return hamur_bul(parsomen_no, min_sira_no, max_sira_no)

    def resolve_blok(self, info, blok_id):
        return blok_getir(blok_id)

    def resolve_bloklar(self, info, parsomen_no: int, hamur_no: int, min_sira=0, max_sira=-1, **kwargs):
        bloklar = blok_bul(parsomen_no, hamur_no, min_sira=min_sira, max_sira=max_sira, **kwargs)
        return [BlokSema(item) for item in bloklar]


sorgu_semasi = Schema(query=Query)
