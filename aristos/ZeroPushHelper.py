__author__ = 'pedrocontreras'
ANDROID_AUTH_KEY = "gcmdev_8MAgVC5GK9q2JPFQPyYu";
BROADCAST_URL = "https://api.zeropush.com/broadcast";
IOS_AUTH_KEY = "iosdev_vroTtM7EFNBsD6q9SUW6";
ANDROID_AUTH_KEY = "gcmdev_8MAgVC5GK9q2JPFQPyYu";


import requests


def sendBroadcastNotification(alert, message, id_circ, tipo):
    data = "{\"idCircular\":" + str(id_circ) + ", \"tipo\":\"" + tipo + "\", \"titulo\":\"" + message + "\"}";

    payload = {'auth_token': IOS_AUTH_KEY,
               'badge': '+1',
               'sound': ' ',
               'alert': alert + ': ' + message,
               'info': data,
               'collapse_key': 'friend_request',
               'delay_while_idle': 'false',
               'time_to_live': '40320'
    }

    payloadAndroid = {
        'auth_token': ANDROID_AUTH_KEY,
        'data[alert]': alert,
        'data[message]': data,
        'collapse_key': 'friend_request',
        'delay_while_idle': 'false',
        'time_to_live': '40320'
    }

    s = requests.post(
        BROADCAST_URL,
        payloadAndroid
    )

    r = requests.post(
        BROADCAST_URL,
        payload
    )

    print r.content
    print s.content