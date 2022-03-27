from config.templates import templates
import graphene
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from starlette_graphene3 import GraphQLApp, make_playground_handler
from controllers.UsuarioGqlController import UsuarioQuery, UsuarioMutation
from controllers.LoginGqlController import LoginQuery, LoginMutation

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')

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

@app.get('/prueba', response_class=HTMLResponse)
def prueba(req: Request):
    ctx = {
        'request': req,
        'data': "hola desde jinja2"
    }
    return templates.TemplateResponse('index.html', ctx)


@app.get('/perros', response_class=HTMLResponse)
def perros(req: Request):
    ctx = {
        'request': req,
        'data': "hola desde peerros"
    }
    return templates.TemplateResponse('perros.html', ctx)