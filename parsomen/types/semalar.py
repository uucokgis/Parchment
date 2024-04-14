from datetime import datetime

from graphene import ObjectType, String, Int, ID, Field, Boolean, InputObjectType, List, DateTime


class CizimAyarlariSema(ObjectType):
    renk = String(description="Renk kodunu temsil eder")
    buyukluk = Int(description="Çizim büyüklüğünü temsil eder")
    font = String(description="Font ismini temsil eder")


class MetinAyarlariSema(CizimAyarlariSema):
    pass


class ParsomenAyarSema(ObjectType):
    _id = ID(required=True)
    parsomenNo = Int(required=True)
    sonYer = Int(default_value=-1)
    cizimAyarlari = Field(CizimAyarlariSema)
    metinAyarlari = Field(MetinAyarlariSema)
    sayfaliMi = Boolean()
    satirliMi = Boolean()


class ParsomenAyarInputSema(InputObjectType):
    pass


class HamurSema(ObjectType):
    _id = ID()
    parsomenNo = Int(description="Parsomen ID")
    bloklar = List(Int, description="Doğru sırayla Blok id'leri")
    siraNo = Int(description="Sıra numarası")


class IcerikSema(ObjectType):
    tipi = String(required=True)
    data = String(required=True)


class BlokSema(ObjectType):
    _id = ID(required=True)
    icerik = Field(IcerikSema, required=True, name='icerik')
    sira = Int(required=True)
    yer = Int(required=True)
    uretilmeTarihi = DateTime(default_value=datetime.now())
    duzenlenmeTarihi = DateTime(default_value=datetime.now())
