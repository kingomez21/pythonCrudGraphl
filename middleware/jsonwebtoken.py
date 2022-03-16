from jose import jwt
from config.env import variables

key = variables['SECRET']

def generarToken(datos: dict):
    if key:
        encode = jwt.encode(datos, key)
        return encode
    else:
        return False


def inLogin(token: str):
    if token and key:
        decode = jwt.decode(token, key, algorithms=['HS256'])
        return decode
    else: 
        return False

