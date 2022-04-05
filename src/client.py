import requests

class Client:
    def __init__(self):
        self.URL = "http://f814-138-67-68-28.ngrok.io/"
        self.json = { 'motor_angle': None }

    def send_request(self, command):
        self.json['motor_angle'] = command.motor_angle
        url = "%s%s" % (self.URL, command.motor)

        resp = requests.post(url, json = self.json)
        return resp
