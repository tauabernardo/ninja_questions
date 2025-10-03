import requests

url = 'http://127.0.0.1:8000/cadastro/api/file'

with open('55.png', 'rb') as f:
    files = {'file': f}
    response = requests.post(url, files=files)

print(response.text)
