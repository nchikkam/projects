import requests
import json
from pprint import pprint

import unittest

class TestRestAPI(unittest.TestCase):

	def test_get_list_authorized_case(self):
		url = 'http://127.0.0.1:5000/us/rawdata/1.0/searchitems'
		r = requests.get(url,
				auth=requests.auth.HTTPBasicAuth(
				'bdusr',
				'bdpwd')
		)
		self.assertEqual(r.status_code, 200)
		pprint(r.text)

	def test_get(self):
		url = 'http://127.0.0.1:5000/us/rawdata/1.0/searchitems/2'
		r = requests.get(url,
				auth=requests.auth.HTTPBasicAuth(
				'bdusr',
				'bdpwd')
		)
		self.assertEqual(r.status_code, 200)
		pprint(r.text)

	def test_post(self):
		url = 'http://127.0.0.1:5000/us/rawdata/1.0/searchitems'

		post_data = {
			"search_word": "ss"
		}

		headers = {'Content-Type': 'application/x-www-form-urlencoded'}
		r = requests.post(url,
				auth=requests.auth.HTTPBasicAuth(
				'bdusr',
				'bdpwd'),
              data=post_data, headers=headers
		)
		self.assertEqual(r.status_code, 200)
		pprint(r.text)

if __name__ == "__main__":
	unittest.main()
