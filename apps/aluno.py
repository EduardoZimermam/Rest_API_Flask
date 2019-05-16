# -*- coding: utf-8 -*-

from flask import request, Response
from bson import json_util

def aluno_api(app, collection):

	@app.route('/aluno', methods=['POST', 'DELETE'])
	def aluno():
		if request.method == 'POST':
			payload = request.get_json()

			if 'nome' in payload:

				collection.insert_one(payload)
				
				return json_util.dumps(payload)
			else:
				return Response('{"messageError": "Faltam campos no payload da requisição"}', status=403)


		if request.method == 'DELETE':

			ra = request.args.get('ra')
			campus = request.args.get('campus')
			
			try:

				if (collection.find_one({'ra': ra, 'campus': campus})):
					
					collection.delete_one({'ra': ra, 'campus': campus})

					return Response("", status=200)
				else:
					return Response('{"data": "Documento não existe"}', status=403)
			except KeyError:
				return Response("", status=404)
