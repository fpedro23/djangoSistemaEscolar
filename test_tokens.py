__author__ = 'mng687'
import requests
import json

SECRET = 'qaDPVnEdTB;:lcXtsNN4Mb9zuSUc_HQ4;ZZ!qC-ZpWb4r8dpfkzzB0kosHHet@sDo5FW:YJc==CpPknC35L7;!cCly7JF7tao:_RsV9vkQDZoesdxV?5VLJN5?.2rD!;'

payload = {
    'grant_type': 'password',
    'username': 'pedro',
    'password': 'pedro',
    'client_id': '?jrsf4IFEFE@3@;_aWWQyWm=NvUBVA.@dN!kcKwr',
    'client_secret': SECRET,
    'scope': 'write read'
}
print requests.post('http://localhost:8000/o/token/', payload).text
