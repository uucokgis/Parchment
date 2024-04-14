from inspect import Arguments

from graphene import ObjectType, Int, String, Mutation, Schema, Field

from parsomen.db.collections import BlokCollection
from parsomen.types.classes import Blok
from parsomen.types.semalar import BlokSema


class BlokQuery(ObjectType):
    blok = Field(BlokSema, required=True, name='blok')

    class GetById(Arguments):
        _id = String(required=False, name='id')

    class GetByHierarchy(Arguments):
        parsomen_no = Int(required=True)
        hamur_no = Int(required=True)
        min_sira = Int(default_value=0)
        max_sira = Int(default_value=-1)

    def resolve_by_id(self, _id):
        return BlokCollection.query(_id=_id)

    # Output = Blok


class BlokMutation(Mutation):
    Output = Blok

    async def mutate(self, info, parsomen_no, hamur_no, min_sira, max_sira, yer):
        pass

    async def mutate(self, info, ):
        pass


blok_sema = Schema(query=BlokQuery)
