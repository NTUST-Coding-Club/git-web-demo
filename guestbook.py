import json
from bottle import run, route, template, static_file, view, request, redirect

@route('/')
@view('static/index.html')
def index():
	try:
		with open('data.json', 'r') as fin:
			posts = json.load(fin)
	except FileNotFoundError as e:
		posts = []
	return { 'posts': posts }

@route('/static/<filename:path>')
def static(filename):
	return static_file(filename, root='static')

@route('/post', method='POST')
def create_post():
	author = request.forms.get('author')
	message = request.forms.get('message')
	post = {
		'author': author,
		'message': message
	}

	try:
		with open('data.json', 'r') as fin:
			posts = json.load(fin)
	except FileNotFoundError as e:
		posts = []

	posts.append(post)

	with open('data.json', 'w') as fout:
		json.dump(posts, fout)

	return redirect('/')

run()
