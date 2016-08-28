import requests
import json
from pprint import pprint

import unittest

class TestRestAPI(unittest.TestCase):
	url = 'http://127.0.0.1:8080/us/rawdata/1.0/searchitems'

	def test_get_list_authorized_case(self):
		r = requests.get(self.url,
				auth=requests.auth.HTTPBasicAuth(
				'dummy',
				'dummy')
		)
		self.assertEqual(r.status_code, 200)

	def test_get_list_unauthorized_case(self):
		r = requests.get(self.url,
				auth=requests.auth.HTTPBasicAuth(
				'',
				'')
		)
		self.assertEqual(r.status_code, 401)

	def test_get(self):
		r = requests.get(self.url+"/2",
				auth=requests.auth.HTTPBasicAuth(
				'dummy',
				'dummy')
		)
		self.assertEqual(r.status_code, 200)

	def test_post(self):
		post_data = {
			"search_word": "ss"
		}
		headers = {'Content-Type': 'application/x-www-form-urlencoded'}
		r = requests.post(self.url,
				auth=requests.auth.HTTPBasicAuth(
				'dummy',
				'dummy'),
              data=post_data, headers=headers
		)
		self.assertEqual(r.status_code, 200)

	### Verifying response
	def test_searchitems_slash_x_respects_requested_number(self):
		l = list(range(10))
		for expected in l:
			url = "{}/{}".format(self.url, expected)
			r = requests.get(url,
							 auth=requests.auth.HTTPBasicAuth(
								 'dummy',
								 'dummy')
							 )
			self.assertEqual(
				expected,
				len(json.loads(r.text)['items'])
			)

	def test_no_sideeffects_for_calls(self):
		response_one = requests.get(self.url,
			auth=requests.auth.HTTPBasicAuth(
			 'dummy',
			 'dummy')
			)

		response_two = requests.get(self.url,
			auth=requests.auth.HTTPBasicAuth(
				'dummy',
				'dummy')
			)

		self.assertEqual(
			response_one.text,
			response_two.text
		)

	def test_post_reponse(self):
		search_word = "ed"
		post_data = {
			"search_word": search_word
		}
		headers = {'Content-Type': 'application/x-www-form-urlencoded'}
		r = requests.post(self.url,
						  auth=requests.auth.HTTPBasicAuth(
							  'dummy',
							  'dummy'),
						  data=post_data, headers=headers
						  )
		data = json.loads(r.text)
		for phrase in data:
			self.assertTrue(search_word in phrase['data'])

	## bad cases

	def test_get_list_bad_case(self):
		r = requests.get(self.url+"/RandomString",
						 auth=requests.auth.HTTPBasicAuth(
							 'dummy',
							 'dummy')
						 )
		self.assertEqual(r.status_code, 404)

if __name__ == "__main__":
	unittest.main()