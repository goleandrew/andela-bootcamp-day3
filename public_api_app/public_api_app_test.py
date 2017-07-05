import unittest, requests
from public_api_app import fetch_data

class HTTPAPITest(unittest.TestCase):
	url = "https://jsonplaceholder.typicode.com/todos/"
	title = "sample title"
	body = "sample body"

	def test_get_returns_nothing_to_show_out_of_range(self):
		"""
		should return '* Nothing to show *' if
		input is not within 1 and 200
		"""
		self.assertEqual("* Nothing to show *",
			fetch_data(self.url, "201"))

	def test_get_raises_value_error_for_non_int(self):
		"""
		should raise Value Error if input is not integer
		"""
		with self.assertRaises(ValueError):
			fetch_data(self.url, "s")

	def test_correct_get_returns_response_object(self):
		"""
		A correct get request should return Response object
		"""
		self.assertIsInstance(fetch_data(self.url, "3"), requests.models.Response)
		
if __name__ == '__main__':
	unittest.main()