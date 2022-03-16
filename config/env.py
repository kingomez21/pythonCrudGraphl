from tkinter import Variable
from dotenv import dotenv_values, load_dotenv

env = load_dotenv('.env')

variables: any

if env:
    variables = dotenv_values('.env')
else:
    print('error en variables de entorno')