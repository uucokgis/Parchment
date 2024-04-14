from graphene import Mutation, String, List, Field, Int, ObjectType

from parsomen.db.parsomen import yeni_parsomen, parsomen_guncelle, parsomen_ara
from parsomen.semalar.parsomen_ayar import ParsomenAyarAyar
from parsomen.semalar.hamur import Hamur
from parsomen.semalar.parsomen import Parsomen


class ParsomenAra(ObjectType):
    class Arguments:
        baslik = String(required=True)

    def baslikla_ara(self, baslik: str):
        return parsomen_ara(baslik=baslik)


class ParsomenUret(Mutation):
    class Arguments:
        baslik = String(required=True)
        hamurlar = List(Hamur, required=True)
        ayar = Field(ParsomenAyarAyar, required=True)

    Output = Parsomen

    async def mutate(self, info, baslik, hamurlar, ayar):
        parsomen = await yeni_parsomen(baslik, hamurlar, ayar)
        return parsomen


class ParsomenGuncelle(Mutation):
    class Arguments:  # all optional
        parsomen_id = Int(required=True)
        baslik = String(required=False)
        hamurlar = List(Hamur, required=False)
        ayar = Field(ParsomenAyarAyar, required=False)

    async def mutate(self, info, parsomen_no, **kwargs):
        return await parsomen_guncelle(parsomen_no, **kwargs)