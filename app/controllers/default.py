from flask import render_template
from app import app, db

from app.models.tables import User

@app.route('/home')
@app.route('/index')
@app.route('/')
def home():
	return "Hello world!"

@app.route('/<name>')
def index(name):
	return '<h1>Hellow {}!<h1>'.format(name)

@app.route("/teste/<info>")
@app.route("/teste", defaults={"info":None})
def teste(info):
	i = User("maria", "1234", "Julia Rizza",
		"maria@gmail.com")
	db.session.add(i)
	db.session.commit()
	return 'ok'