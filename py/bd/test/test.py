import requests
import json
from pprint import pprint

import unittest

class TestRestAPI(unittest.TestCase):

	def test_get_list_unauthorized_case(self):
		url = 'http://127.0.0.1:5000/todo/api/v1.0/tasks'
		r = requests.get(url)
		self.assertEqual(r.status_code, 401)
		pprint(r.text)

	def test_get_list_authorized_case(self):
		url = 'http://127.0.0.1:5000/todo/api/v1.0/tasks'
		r = requests.get(url,
				auth=requests.auth.HTTPBasicAuth(
				'bdusr',
				'bdpwd')
		)
		self.assertEqual(r.status_code, 200)
		pprint(r.text)

	def test_get(self):
		url = 'http://127.0.0.1:5000/todo/api/v1.0/tasks/1'
		r = requests.get(url)
		self.assertEqual(r.status_code, 200)
		pprint(r.text)

	def test_get_error(self):
		url = 'http://127.0.0.1:5000/todo/api/v1.0/tasks/79'
		r = requests.get(url)
		self.assertEqual(r.status_code, 404)
		pprint(r.text)


	def test_post(self):
		url = 'http://127.0.0.1:5000/todo/api/v1.0/tasks'

		post_data = {
			"description": "",
			"done": False,
			"id": 3,
			"title": "Read a book"
		}

		headers = {'Content-Type': 'application/json'}
		r = requests.post(url,
              data=json.dumps(post_data), headers=headers
		)
		self.assertEqual(r.status_code, 201)   # http standard code for created
		pprint(r.text)

	def test_put(self):
		url = 'http://127.0.0.1:5000/todo/api/v1.0/tasks/2'  # updating task to Done

		post_data = {
			"done": True,					# False to True
		}

		headers = {'Content-Type': 'application/json'}
		r = requests.put(url,
              data=json.dumps(post_data), headers=headers
		)
		self.assertEqual(r.status_code, 200)   # http standard code for created
		pprint(r.text)

	def test_delete(self):
		url = 'http://127.0.0.1:5000/todo/api/v1.0/tasks/2'  # updating task to Done

		headers = {'Content-Type': 'application/json'}
		r = requests.delete(url, headers=headers)
		self.assertEqual(r.status_code, 200)   # http standard code for created
		pprint(r.text)




if __name__ == "__main__":
	unittest.main()
