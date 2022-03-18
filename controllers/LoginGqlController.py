import graphene
from middleware.jsonwebtoken import generarToken, inLogin

class UsuarioLogin(graphene.ObjectType):
    email = graphene.String()
    password = graphene.String()


class LoginInput(graphene.InputObjectType):
    email = graphene.String(required=True)
    password = graphene.String(required=True)


class Login(graphene.Mutation):
    token = graphene.String()
    class Arguments:
         login = LoginInput()

    def mutate(parent, info, login=None):
        lg = {"email": login.email, 'password': login.password}
        _token = generarToken(lg)
        return Login(token=_token)


#MUTATIONS
class LoginMutation(graphene.ObjectType):
    LoginUsers = Login.Field()


#QUERYS
class LoginQuery(graphene.ObjectType):
    getToken = graphene.Field(UsuarioLogin, token=graphene.String())
    
    def resolve_getToken(parent, info, token):
        data = inLogin(token)
        return data