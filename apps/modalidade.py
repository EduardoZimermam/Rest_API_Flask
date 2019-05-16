# -*- coding: utf-8 -*-

from flask import request
from bson import json_util

def modalidade_api(app, collection):

	@app.route('/modalidade', methods=['GET'])
	def modalidade():
		# Faz o get dos parâmetros passados pela URL
		modalidade = request.args.get('modalidade')
		data_inic = request.args.get('data_inicio')
		data_fim = request.args.get('data_fim')

		# Monta a query para execução
		query = {'modalidade': modalidade, 'data_inicio': {'$gte': data_inic, '$lte': data_fim}}

		# Execução e retorno do resultado da query
		return json_util.dumps(collection.find(query, {'nome': 1, 'data_inicio': 1, '_id': 0}).sort('data_inicio', 1))