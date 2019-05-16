# -*- coding: utf-8 -*-

from flask import request
from bson import json_util

def aluno_api(app, collection):

	@app.route('/aluno', methods=['POST', 'DELETE'])
	def aluno():
		if request.method == 'POST':
			payload = request.get_json()

			collection.insert_one(payload)

			return json_util.dumps(payload)


		if request.method == 'DELETE':

			ra = request.args.get('ra')
			campus = request.args.get('campus')
			
			try:

				if (collection.find_one({'ra': ra, 'campus': campus})):
					
					collection.delete_one({'ra': ra, 'campus': campus})

					return json_util.dumps({"status": "200", "data": "SUCESS"})
				else:
					return json_util.dumps({"status": "403", "data": "Documento não existente"})
			except KeyError:
				return json_util.dumps({"status": "404", "data": "Parâmetros errados"})
