import graphene
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette_graphene3 import GraphQLApp, make_playground_handler
from schema import Query, Mutation, Subscription

app = FastAPI()

app.add_middleware(CORSMiddleware, 
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
)

schema = graphene.Schema(query=Query, mutation=Mutation, subscription=Subscription)

app.add_route('/gql', GraphQLApp(schema=schema,context_value=Request ,on_get=make_playground_handler()))
