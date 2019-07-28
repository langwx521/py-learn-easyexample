import unittest

class TestMethod(unittest.TestCase):
	
	@classmethod
	def setUpClass(cls):
		print("behind the class to run ")

	@classmethod
	def tearDownClass(cls):
		print("after the clas  to run ")		

	def setUp(self):
		print("test-->setUp")
	
	def tearDown(self):
		print("test-->tearDown")

	def test_01(self):
		print("This is a test method!")

	def test_02(self):
		print("This is a test method two!")

if __name__ == '__main__':
	 unittest.main()

