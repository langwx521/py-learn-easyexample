import unittest

class TestMethod(unittest.TestCase):

		
		def setUp(self):
			print('test --> setUp')

		def tearDown(self):
			print('test --> tearDown')

		def test_01(self):
			print('这是测试方法-01')

		def test_02(self):
			print('这是测试方法-02')



if __name__ == '__main__':
	unittest.main()