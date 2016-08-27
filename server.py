from engine.render import render
from tornado.server import Server


def render_page(filename, response, context):
	html = render(filename, context)
	response.write(html)


def index_handler(response):
	render_page('index.html', response, {})


def error_handler(response):
	response.set_status(404)
	render_page('404.html', response, {})


if __name__ == '__main__':
	server = Server()

	mappings = [
		(r'/', index_handler),
		(r'/.*', error_handler)
	]

	for url, callback in mappings:
		server.register(url, callback)

	server.run()
