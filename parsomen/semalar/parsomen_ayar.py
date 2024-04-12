from graphene import ObjectType, String, Int, Boolean, InputObjectType, Field, ID
from graphene import Schema

from parsomen.db.parsomen_ayar import persomen_ayar_bul, parsomen_ayar_guncelle


class CizimAyarlari(ObjectType):
    renk = String(description="Renk kodunu temsil eder")
    buyukluk = Int(description="Çizim büyüklüğünü temsil eder")
    font = String(description="Font ismini temsil eder")


class MetinAyarlari(CizimAyarlari):
    pass


class BaseParsomenAyar:
    _id = ID(required=True)
    parsomenNo = Int(required=True)
    sonYer = Int(default_value=-1)
    cizimAyarlari = Field(CizimAyarlari)
    metinAyarlari = Field(MetinAyarlari)
    sayfaliMi = Boolean()
    satirliMi = Boolean()


class ParsomenAyarInput(InputObjectType, BaseParsomenAyar):
    pass


class ParsomenAyar(ObjectType, BaseParsomenAyar):
    @staticmethod
    def ayar_getir(parsomen_no=-1):
        ayar = persomen_ayar_bul(parsomen_no)
        if ayar is not None:
            return ParsomenAyar(**ayar)
        return None


class Mutation(ObjectType):
    parsomen_no = Int(required=True, description="Parsomen no.")
    parsomen_ayar = Field(ParsomenAyar, input=ParsomenAyarInput(required=True))

    async def update_ayar(self, info, parsomen_no, parsomen_ayar):
        await parsomen_ayar_guncelle(parsomen_no, parsomen_ayar)


ayarlar_sema = Schema(query=ParsomenAyar)
