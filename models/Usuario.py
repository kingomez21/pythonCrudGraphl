from sqlalchemy import  Column, Table
from sqlalchemy.sql.sqltypes import Integer, String, Date
from config.db import meta, engine

users = Table('usuario',meta,
        Column('id', Integer, primary_key=True),
        Column('identificacion', Integer),
        Column('nombres', String(255)),
        Column('fecha_nacimiento', Date) 
        )


meta.create_all(engine)