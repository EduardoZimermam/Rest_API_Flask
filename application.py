# -*- coding: utf-8 -*-

from os import getenv
from os.path import dirname, isfile, join

from dotenv import load_dotenv


# Adiciona ao path
__ENV_FILE = join(dirname(__file__), '.env')


# Faz o load do arquivo 
if isfile(__ENV_FILE):
	load_dotenv(dotenv_path=__ENV_FILE)

from apps import create_app
from apps.aluno import aluno_api
from apps.modalidade import modalidade_api
from apps.campus import campus_api
from pymongo import MongoClient
from flask_swagger_ui import get_swaggerui_blueprint

app = create_app(getenv('FLASK_ENV') or 'default')

collection = MongoClient(getenv('MONGO_URL'), int(getenv('MONGO_PORT'))).eduardo_zimermam_pereira.estudantes

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
	getenv('SWAGGER_URL'),
	getenv('SWAGGER_API_URL'),
	config={'app_name': "Desafio Full Stack Laura"},
)

# Register blueprint at URL
# (URL must match the one given to factory function above)
app.register_blueprint(swaggerui_blueprint, url_prefix=getenv('SWAGGER_URL'))

aluno_api(app, collection)
modalidade_api(app, collection)
campus_api(app, collection)


if __name__ == '__main__':
	ip = getenv('API_URL')
	debug = app.config['DEBUG']
	port = app.config['APP_PORT']

	app.run(
		host=ip, debug=debug, port=port, use_reloader=debug
	)