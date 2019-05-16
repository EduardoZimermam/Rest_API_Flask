# -*- coding: utf-8 -*-

from flask import jsonify, request, app

def aluno_api(app, collection):

	@app.route('/', methods=['GET', 'POST'])
	def aluno():
		if request.method == 'GET':
			return jsonify({'aluno': 'Eduardo Zimermam Pereria'})
		
		if request.method == 'POST':
			return jsonify({'aluno': 'CRIADO'})