import requests

class Client:
    def __init__(self):
        self.URL = "http://6859-138-67-78-54.ngrok.io/"
        self.json = { 'motor_angle_update': None }

    def send_request(self, command):
        self.json['motor_angle_update'] = command.motor_angle
        url = "%s%s" % (self.URL, command.motor)

        resp = requests.post(url, json = self.json)
        return resp
