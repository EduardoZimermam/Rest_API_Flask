# -*- coding: utf-8 -*-

from flask import request
from bson import json_util

def campus_api(app, collection):

	@app.route('/campus/cursos', methods=['GET'])
	def cursos_campus():
		# Faz o get dos parâmetros passados pela URL
		campus = request.args.get('campus')

		# Monta a query para execução
		query = {'campus': campus}

		# Execução e retorno do resultado da query
		return json_util.dumps(collection.find(query, {'curso': 1, '_id': 0}).distinct('curso'))

	@app.route('/campus/quantidade_alunos', methods=['GET'])
	def quantidade_alunos_campus():
		# Faz o get dos parâmetros passados pela URL
		campus = request.args.get('campus')
		data_inic = request.args.get('data_inicio')
		data_fim = request.args.get('data_fim')

		# Monta a query para execução
		query = {'campus': campus, 'data_inicio': {'$gte': data_inic, '$lte': data_fim}}

		# Execução e retorno do resultado da query
		return json_util.dumps({'total_alunos': collection.find(query).count()})