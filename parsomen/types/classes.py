import enum
from abc import ABC
from dataclasses import dataclass
from datetime import datetime

from bson import ObjectId


class Base(ABC):
    _id: ObjectId
    uretilmeTarihi: datetime
    duzenlenmeTarihi: datetime


@dataclass
class Blok(Base):
    icerik: dict
    sira: int
    yer: int


class IcerikTipi(enum.Enum):
    Raster = 'Raster'
    Metin = 'Metin'


@dataclass
class Icerik:
    tip: IcerikTipi
    data: str


@dataclass
class Hamur(Base):
    parsomenNo: int
    bloklar: list[int]
    sira: int


@dataclass
class Parsomen(Base):
    parsomenNo: int
    baslik: str
    hamurlar: list[int]
    ayarNo: int


@dataclass
class CizimAyarlari:
    renk: str
    buyukluk: int
    font: str


@dataclass
class MetinAyarlari(CizimAyarlari):
    pass


@dataclass
class ParsomenAyar(Base):
    parsomenNo: int
    sonYer: int
    cizimAyarlari: CizimAyarlari
    metinAyarlari: MetinAyarlari
    sayfaliMi: bool
    satirliMi: bool
