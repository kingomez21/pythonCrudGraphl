import graphene
from config.db import conexion
from models.Usuario import users
from graphene_file_upload.scalars import Upload
from middleware.jsonwebtoken import generarToken, inLogin


#TYPES
class Usuario(graphene.ObjectType):
    id = graphene.Int()
    identificacion = graphene.Int()
    nombres = graphene.String()
    fecha_nacimiento = graphene.Date()


class UsuarioLogin(graphene.ObjectType):
    email = graphene.String()
    password = graphene.String()


#INPUTS TYPE
class Input_Persona(graphene.InputObjectType):
    name = graphene.String(required=True)
    lastname = graphene.String(required=True)


class UserInput(graphene.InputObjectType):
    id = graphene.Int()
    identificacion = graphene.Int()
    nombres = graphene.String()
    

class LoginInput(graphene.InputObjectType):
    email = graphene.String(required=True)
    password = graphene.String(required=True)



#MUTATE
class Create_persona(graphene.Mutation):
    class Arguments:
        person = Input_Persona(required=True)
    
    message = graphene.String()

    def mutate(parent, info, person=None):
        data = {"name": person.name, "lastname": person.lastname}
        print(data)
        return Create_persona(message="Guardado exitosamente")


class FileUploadMutation(graphene.Mutation):
    class Arguments:
        file = Upload()

    ok = graphene.Boolean()

    def mutate(self, info, file, **kwargs):
        print(file)
        return FileUploadMutation(ok=True)


class CrearUsuario(graphene.Mutation):
    class Arguments:
        user = UserInput()

    mensaje = graphene.String()

    def mutate(parent, info, user=None):
        data = {'identificacion': user.identificacion, 'nombres': user.nombres}
        conexion.execute(users.insert().values(data))
        return CrearUsuario(mensaje="guardado exitosamente")


class Login(graphene.Mutation):
    token = graphene.String()
    class Arguments:
         login = LoginInput()

    def mutate(parent, info, login=None):
        lg = {"email": login.email, 'password': login.password}
        _token = generarToken(lg)
        return Login(token=_token)
