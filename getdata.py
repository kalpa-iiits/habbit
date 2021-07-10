import requests
import json

URL = "http://127.0.0.1:8000/api/course/"


def get_data(id=None):
	data = {}
	if id is not None:
		data = {'id': id}

	json_data = json.dumps(data)
	r = requests.get(url=URL, data= json_data)
	response = r.json()
	print(response)

get_data()
