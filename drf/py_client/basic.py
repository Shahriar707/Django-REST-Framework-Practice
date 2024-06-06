import requests 

endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.post(endpoint, params={"key": 123}, json={"title": "Hello World!", 'content': 'Now you see me!'})

print(get_response.text)
print(get_response.status_code)
print(get_response.json())