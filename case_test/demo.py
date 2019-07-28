import requests
import json
class RunMain:
	# """docstring for RunMain"""
	# def __init__(self, arg):
	# 	super(RunMain, self).__init__()
	# 	self.arg = arg

	def send_get(self,url,data):
		# res = requests.get(url=url,data=data).json
		res = requests.get(url=url,data=data)
		return res

	def send_post(self,url,data):
		res = requests.post(url=url,data=data).json
		return res

	def run_main(self,url,method,data=None):
		res = None
		if method == 'GET':
			res = self.send_get(url,data)
		else:
			res = self.send_post(url,data)
		return res

if __name__ == '__main__':
	url = 'http://www.imooc.com/m/web/shizhangapi/loadmorepingjia.html?cart=11'
	data = {
		'cart':'11'
	}

	# run = RunMain(url,'GET',data)
	# print(run.res)
	# unittest
	run = RunMain()
	res1 =run.run_main(url,'GET',data)
	# print(json.load(res1))

	print(res1)
	# print(run.res)