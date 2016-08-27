import os

from tornado.server import Server
from data.data import all_produce
from jinja2 import Environment, FileSystemLoader

template_path = os.path.join(os.path.dirname(__file__), 'templates')
env = Environment(loader=FileSystemLoader(template_path), trim_blocks=True, lstrip_blocks=True)


def render_page(filename, response, context):
	default_context = {'query': None}

	for var, value in default_context.items():
		if var not in context:
			context[var] = value

	html = env.get_template(filename).render(**context)
	response.write(html)


def index_handler(response):
	render_page('index.html', response, {})


def search_handler(response):
	context = {}
	render_page('search-result.html', response, context)


def produce_handler(response, produce_id):
	context = {}
	produce = all_produce.find_id(produce_id)

	if not produce:
		error_handler(response)
		return

	context['produce'] = produce
	render_page('produce.html', response, context)


def error_handler(response):
	response.set_status(404)
	render_page('404.html', response, {})


def dashboard_handler(response):

	widgets = [
		('Messages', 'messages', 'account/messages'),
		('Profile', 'profile', 'account/profile'),
		('My Marks', 'my-marks', 'account/marks'),
		('My Patch', 'my-patch', 'account/patch'),
		('Mark Favs', 'mark-favs', 'account/mark-favs'),
		('Community', 'social-community', '#'),
		('Food Favs', 'food-favs', 'account/food-favs'),
		('History', 'my-history', 'account/history'),
		('Food for Thought', 'food-for-thought', '#'),
		('Research', 'research', 'research'),
		('Market Analytics', 'market-analytics', '#'),
		('Account Settings', 'settings', 'account/settings'),
	]

	render_page('dashboard.html', response, {'widgets': widgets})


if __name__ == '__main__':
	server = Server()
	server.register(r'/', index_handler)

	server.register(r'/produce/search', search_handler)
	server.register(r'/produce/(\d+)', produce_handler)

	server.register(r'/account/dashboard', dashboard_handler)
	server.register(r'/.*', error_handler)
	server.run()
