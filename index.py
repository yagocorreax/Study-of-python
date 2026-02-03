import requests

BASE_URL = 'http://api.github.com'

def selecionarusuario(username):
    url = f'{BASE_URL}/users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None