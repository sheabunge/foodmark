import csv


class Produce:

	def __init__(self):
		self.produce = [item for item in load_data('produce')]

	def find_id(self, produce_id):
		return self.produce[produce_id]


def load_data(filename):
	file = open('data/{}.csv'.format(filename))
	return csv.DictReader(file)

all_produce = Produce()

