from bson import ObjectId
from graphene import ObjectType, Int, String, Mutation, Schema, Field, ID, List

from parsomen.db.collections import BlokCollection
from parsomen.types.classes import Blok, Icerik
from parsomen.types.semalar import BlokSema


class BlokQuery(ObjectType):
    blok_by_id = Field(BlokSema, _id=ID(required=True), description='Find blok by id')
    blok_by_hierarchy = List(BlokSema, parsomen_no=Int(required=True),
                             hamur_no=Int(required=True),
                             min_sira=Int(default_value=0),
                             max_sira=Int(default_value=-1), description='Find blok by hierarchy')

    def resolve_blok_by_id(self, info, _id):
        blok = BlokCollection.query(True, _id=ObjectId(_id))
        print(blok)
        return blok

    def resolve_blok_by_hierarchy(self, info, parsomen_no, hamur_no, min_sira, max_sira):
        blok = list(BlokCollection.query_with_hierarchy(parsomen_no, hamur_no, min_sira, max_sira))
        print(blok)
        return blok

    Output = BlokSema


class BlokMutation(Mutation):
    Output = Blok
    blok = Field(BlokSema, _id=ID(required=True))

    async def mutate(self, info, parsomen_no, hamur_no, icerik, sira, yer):
        icerik = Icerik(icerik)
        item = Blok(icerik=icerik, sira=sira, yer=yer)
        blok = BlokCollection.create()

    async def mutate(self, info, ):
        pass


blok_sema = Schema(query=BlokQuery)
