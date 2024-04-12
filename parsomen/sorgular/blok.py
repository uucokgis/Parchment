from graphene import Mutation, List, Field, Int, ObjectType

from parsomen.db.blok import yeni_blok, blok_guncelle, blok_bul
from parsomen.semalar.blok import Icerik, BlokSema
from parsomen.semalar.hamur import Hamur


class BlokUret(Mutation):
    class Arguments:
        icerik = Field(Icerik, required=True)
        sira = Int(required=True)
        yer = Int(required=True)

    Output = BlokSema

    async def mutate(self, icerik: Icerik, sira, yer):
        return await yeni_blok(icerik_tipi=icerik.tipi, veri=icerik.data, sira_no=sira, yer=yer)


class BlokGuncelle(Mutation):
    class Arguments:  # all optional
        blok_id = Int(required=False)
        parsomen_no = Int(required=False)
        hamur_no = Int(required=False)

    async def mutate(self, info, blok_id, blok):
        return await blok_guncelle(blok_id=blok_id, blok=blok)

    async def mutate(self, info, parsomen_no, hamur_no, sira_no=None, yer=None):
        return await blok_guncelle(parsomen_no, hamur_no, sira_no, yer)


class BlokBul(ObjectType):
    class Arguments:
        parsomen_no = Int(required=True)
        hamur_no = Int(required=True)
        sira_no = Int(default=0)
        yer = Int(default=0)

    class FindByID(Arguments):
        blok_id = Int(required=True)

    def blok_bul_by_details(self, info, parsomen_no, hamur_no, sira_no, yer):
        return blok_bul(parsomen_no, hamur_no, sira_no, yer)

    def blok_bul_by_id(self, info, blok_id):
        return blok_bul(blok_id=blok_id)
