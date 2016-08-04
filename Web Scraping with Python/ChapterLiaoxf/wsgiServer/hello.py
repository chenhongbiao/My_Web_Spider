
def application(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/html')])
	body = '<h1>Hello, %s!</h1>' %(environ['PATH_INFO'][1:] or 'web')
	#Request URL:http://localhost:8000/Meow
	#environ['PATH_INFO'] = /Meow
	return [body.encode('utf-8')]