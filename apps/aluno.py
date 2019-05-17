# -*- coding: utf-8 -*-

from flask import request, Response
from bson import json_util

def aluno_api(app, collection):

	@app.route('/aluno', methods=['POST', 'DELETE'])
	def aluno():
		if request.method == 'POST':
			payload = request.get_json()

			if payload:
				collection.insert_one(payload)
				
				return Response(json_util.dumps(payload), status=201)
			else:
				return Response("", status=403)

		if request.method == 'DELETE':

			ra = request.args.get('ra')
			campus = request.args.get('campus')

			if (collection.find({"ra": ra, "campus": campus})):
				collection.delete_one({'ra': ra, 'campus': campus})
			
				return Response("", status=200)
			