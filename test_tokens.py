__author__ = 'mng687'
import requests

payload = {
    'grant_type': 'password',
    'username': 'pedro',
    'password': 'pedro',
}
print requests.post('http://rPGzzF1xtW4tBd5yG8tzJCZEncEK2e9wpewe4lNe:kjLlRgWc5lNIml00zjrxmssUvUeEAe4Rv5P3vI6aBG0DKVV8epU8Fxfo2mclYKVA03NahzqPdTZX0owOfotWckDm6UX6ub3KuHqfcNWlcvGAppJLZyiHz3xvKeYTrgWt@localhost:8000/o/token/', payload).text
