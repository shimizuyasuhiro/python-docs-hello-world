from bottle import route, default_app

@route('/')
def hello():
    return 'Hello World'

app = default_app()