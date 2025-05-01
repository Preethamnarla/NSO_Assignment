import os
import flask 
import platform
import time
import random
import socket
from ping3 import ping


basedir = os.path.abspath(os.path.dirname(__file__))
data_file = os.path.join(basedir, 'nodes.yaml')

WORDS = []
with open(data_file, "r") as file:
    for line in file.readlines():
        WORDS.append(line.rstrip())
        

app = flask.Flask(__name__)

@app.route('/')
def index():
    Time= time.strftime("%Y-%m-%d %H:%M:%S")
    WORDS = []
    with open(data_file, "r") as file:
        for line in file.readlines():
            node=line.rstrip()
            rtt=str(int(ping(node,timeout=1, unit='ms')))

            if rtt == "0":
                pingStr=Time + " " + node + " N/A"
            else:
                pingStr=Time + " " + node + " " + rtt + " ms"
                
            WORDS.append(pingStr)

    returnStr='\n'.join(WORDS)
    return returnStr + "\n"
    
