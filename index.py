import graphene
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette_graphene3 import GraphQLApp, make_playground_handler
from controllers.UsuarioGqlController import UsuarioQuery, UsuarioMutation
from controllers.LoginGqlController import LoginQuery, LoginMutation

app = FastAPI()

app.add_middleware(CORSMiddleware, 
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Mutation(UsuarioMutation, LoginMutation):
    pass


#QUERYS
class Query(UsuarioQuery, LoginQuery):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)

app.add_route('/gql', GraphQLApp(schema=schema,context_value=Request ,on_get=make_playground_handler()))
