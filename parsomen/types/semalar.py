from graphene import ObjectType, String, Int, ID, Field, Boolean, InputObjectType, List, DateTime

from .classes import *


class CizimAyarlariSema(CizimAyarlari, ObjectType):
    renk = String(description="Renk kodunu temsil eder")
    buyukluk = Int(description="Çizim büyüklüğünü temsil eder")
    font = String(description="Font ismini temsil eder")


class MetinAyarlariSema(CizimAyarlariSema):
    pass


class ParsomenAyarSema(ParsomenAyar, ObjectType):
    _id = ID(required=True)
    parsomenNo = Int(required=True)
    sonYer = Int(default_value=-1)
    cizimAyarlari = Field(CizimAyarlariSema)
    metinAyarlari = Field(MetinAyarlariSema)
    sayfaliMi = Boolean()
    satirliMi = Boolean()


class ParsomenAyarInputSema(ParsomenAyar, InputObjectType):
    pass


class HamurSema(Hamur, ObjectType):
    _id = ID()
    parsomenNo = Int(description="Parsomen ID")
    bloklar = List(Int, description="Doğru sırayla Blok id'leri")
    siraNo = Int(description="Sıra numarası")


class BlokSema(Blok, ObjectType):
    _id = ID(required=True)
    icerik = Field(Icerik, required=True)
    sira = Int(required=True)
    yer = Int(required=True)
    uretilmeTarihi = DateTime(default_value=datetime.now())
    duzenlenmeTarihi = DateTime(default_value=datetime.now())