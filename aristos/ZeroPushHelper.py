__author__ = 'pedrocontreras'
ANDROID_AUTH_KEY = "gcmdev_8MAgVC5GK9q2JPFQPyYu";
BROADCAST_URL = "https://api.zeropush.com/broadcast";
IOS_AUTH_KEY = "iosdev_Rqohwid72sxjNEqkpszG";

import requests

def sendBroadcastNotification(alert, message, id, tipo):

    data = {


    }

    r = requests.post(BROADCAST_URL,)
    print alert
    print(message)
    print(id)
    print(tipo)