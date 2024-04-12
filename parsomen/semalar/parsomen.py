from flask import Flask
from graphene import ObjectType, Schema, Int, String, ID, List

from parsomen.db.parsomen import parsomen_koleksiyonu

app = Flask(__name__)
app.debug = True


class Parsomen(ObjectType):
    _id = ID()
    parsomenNo = Int(required=True)
    baslik = String(required=True)
    hamurlar = List(Int(), name='hamurlar')
    ayar = ID(name='ayar')  # FK

    def resolve_parsomen(self, info, parsomen_no: int):
        return parsomen_koleksiyonu.find_one({"parsomenNo": parsomen_no})


class TextSearch(ObjectType):
    """
    Define functions for::

    Yetenekleri:
    * Metin arama: elasticsearch ile kullanılabilir.
    iki yere bakilacak: parsomen title'lari (daha hızlı gelecektir)
    tüm bloklarin zamana göre siralanmış halde ve tipi: Raster olmayan tüm veri degerine bakılır
"""


# Create a GraphQL schema
parsomen_sema = Schema(query=Parsomen)
