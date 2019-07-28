
import os 
import unittest


class TestOne(unittest.TestCase):
	"""docstring for TestOne"""

	def test_01(self):
		print(os.path)
		print("I love Py")

	def test_02(self):
		print(os.path)
		print("I love mum")
		
if __name__ == '__main__':
	unittest.main()