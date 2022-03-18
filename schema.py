import graphene
import asyncio
from controllers.UsuarioGqlController import UsuarioQuery, UsuarioMutation
from controllers.LoginGqlController import LoginQuery, LoginMutation

#MUTATIONS
class Mutation(UsuarioMutation, LoginMutation):
    pass

#QUERYS
class Query(UsuarioQuery, LoginQuery):
    pass



#SUBSCRIPTIONS
class Subscription(graphene.ObjectType):
    count = graphene.Int(upto=graphene.Int())

    async def subscribe_count(root, info, upto=3):
        for i in range(upto):
            yield i
            await asyncio.sleep(1)