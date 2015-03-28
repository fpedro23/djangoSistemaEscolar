__author__ = 'pedrocontreras'
ANDROID_AUTH_KEY = "gcmdev_8MAgVC5GK9q2JPFQPyYu";
BROADCAST_URL = "https://api.zeropush.com/broadcast";
IOS_AUTH_KEY = "iosdev_vroTtM7EFNBsD6q9SUW6";
ANDROID_AUTH_KEY = "gcmdev_8MAgVC5GK9q2JPFQPyYu";


import requests
import json


def send_broadcast_notification(alert, message, id_circ, tipo):
    data = {
        'idCircular': str(id_circ),
        'tipo': tipo,
        'titulo': message
    }

    payload = {'auth_token': IOS_AUTH_KEY,
               'badge': '+1',
               'sound': ' ',
               'alert': alert + ': ' + message,
               'info': json.dumps(data),
               'collapse_key': 'friend_request',
               'delay_while_idle': 'false',
               'time_to_live': '40320'
    }

    payload_android = {
        'auth_token': ANDROID_AUTH_KEY,
        'data[alert]': alert,
        'data[message]': json.dumps(data),
        'collapse_key': 'friend_request',
        'delay_while_idle': 'false',
        'time_to_live': '40320'
    }

    requests.post(
        BROADCAST_URL,
        payload_android
    )

    requests.post(
        BROADCAST_URL,
        payload
    )