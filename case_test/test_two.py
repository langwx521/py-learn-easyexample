import json

class OperationJson():

	"""docstring for ClassName"""

	def __init__(self, arg):
		pass


	def read_data(self):
		with open('./practice/login.json') as json_file:
			data = json.load(fp)
			return data

	def get_data(self,id):
		return self.