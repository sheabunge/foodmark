import json


class Produce:

	def __init__(self, produce):
		self.produce = produce

	def find_id(self, produce_id):
		return self.produce[produce_id]


def load_data(filename):
	file = open('data/{}.json'.format(filename))
	return json.load(file)


all_produce = Produce(load_data('produce'))

