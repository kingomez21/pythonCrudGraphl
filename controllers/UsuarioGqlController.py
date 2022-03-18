import graphene
from config.db import conexion
from models.Usuario import users
from graphene_file_upload.scalars import Upload


#TYPES
class Usuario(graphene.ObjectType):
    id = graphene.Int()
    identificacion = graphene.Int()
    nombres = graphene.String()
    fecha_nacimiento = graphene.Date()





#INPUTS TYPE
class Input_Persona(graphene.InputObjectType):
    name = graphene.String(required=True)
    lastname = graphene.String(required=True)


class UserInput(graphene.InputObjectType):
    id = graphene.Int()
    identificacion = graphene.Int()
    nombres = graphene.String()
    





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


#MUTATIONS
class UsuarioMutation(graphene.ObjectType):
    CrearPersona = Create_persona.Field()
    filess = FileUploadMutation.Field()
    CreateUser = CrearUsuario.Field()
   

#QUERYS
class UsuarioQuery(graphene.ObjectType):
    hello = graphene.String(name=graphene.String())
    getUsers = graphene.List(Usuario)
    
    
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