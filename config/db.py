from sqlalchemy import create_engine, MetaData
from .env import variables

engine = create_engine(variables["URLCONECTION"])

meta=MetaData()

conexion = engine.connect()

