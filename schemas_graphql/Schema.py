import graphene
import asyncio
from config.db import conexion
from models.Usuario import users
from .typesDef import Usuario, CrearUsuario, Create_persona, FileUploadMutation, Login, UsuarioLogin
from middleware.jsonwebtoken import inLogin

#MUTATIONS
class Mutation(graphene.ObjectType):
    CrearPersona = Create_persona.Field()
    filess = FileUploadMutation.Field()
    CreateUser = CrearUsuario.Field()
    LoginUsers = Login.Field()

#QUERYS
class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String())
    getUsers = graphene.List(Usuario)
    getToken = graphene.Field(UsuarioLogin, token=graphene.String())
    
    def resolve_hello(parent, info, name, **kwargs):
        try:
            token = info.context.headers['aut']
            if token:
                return "hola desde fastApi "+name
            else:
                return "credenciales no validas"
        except:
            print("error")

    def resolve_getUsers(parent, info):
        tok = info.context.headers['aut']
        print(tok)
        data = conexion.execute(users.select()).fetchall()
        return data
    
    def resolve_getToken(parent, info, token):
        data = inLogin(token)
        return data



#SUBSCRIPTIONS
class Subscription(graphene.ObjectType):
    count = graphene.Int(upto=graphene.Int())

    async def subscribe_count(root, info, upto=3):
        for i in range(upto):
            yield i
            await asyncio.sleep(1)