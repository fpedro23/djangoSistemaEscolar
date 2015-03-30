__author__ = 'mng687'
import requests
import json

SECRET = 'kjLlRgWc5lNIml00zjrxmssUvUeEAe4Rv5P3vI6aBG0DKVV8epU8Fxfo2mclYKVA03NahzqPdTZX0owOfotWckDm6UX6ub3KuHqfcNWlcvGAppJLZyiHz3xvKeYTrgWt'

payload = {
    'grant_type': 'password',
    'username': 'pedro',
    'password': 'pedro',
    'client_id': 'rPGzzF1xtW4tBd5yG8tzJCZEncEK2e9wpewe4lNe',
    'client_secret': SECRET,
    'scope': 'write read'
}
print requests.post('http://localhost:8000/o/token/', payload).text
