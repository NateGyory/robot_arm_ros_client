#!/usr/bin/python3

from command import Command
from client import Client

input_dict = {'q': Command('servo1', -1),
              'w': Command('servo1', 1),
              'a': Command('servo2', -1),
              's': Command('servo2', 1),
              'z': Command('servo3', -1),
              'x': Command('servo3', 1),
              'e': Command('servo4', -1),
              'r': Command('servo4', 1),
              'd': Command('servo5', -1),
              'f': Command('servo5', 1)
             }

def get_input():
    command = None
    key = input("\
        q/w: incr/decr servo1\n\
        a/s: incr/decr servo2\n\
        z/x: incr/decr servo3\n\
        e/r: incr/decr servo4\n\
        d/f: incr/decr servo5\n")

    if key in input_dict:
        command = input_dict[key]
    else:
        command = Command("", "", True)
        print('Key does not exist')

    return command

def run():
    client = Client()
    while 1:
        command = get_input()
        if command.error: continue

        resp = client.send_request(command)

        # TODO make a nice table to display all motor states
        print(resp.status_code, resp.content)

##########
#  main  #
##########
run()
