import requests

class Client:
    def __init__(self):
        self.URL = "http://aca5-184-96-73-112.ngrok.io/"
        self.json = { 'motor_angle_update': None }

    def send_request(self, command):
        self.json['motor_angle'] = command.motor_angle
        url = "%s%s" % (self.URL, command.motor)

        resp = requests.post(url, json = self.json)
        return resp
