import requests

class Client:
    def __init__(self):
        self.URL = "http://127.0.0.1:5000/"
        self.json = { 'direction': None }

    def send_request(self, command):
        self.json['direction'] = command.direction
        url = "%s%s" % (self.URL, command.motor)

        resp = requests.post(url, json = self.json)
        return resp
