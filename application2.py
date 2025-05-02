import flask
import time
import socket
h_name = socket.gethostname()
IP_addres = socket.gethostbyname(h_name)

app = flask.Flask(__name__)

@app.route('/')
def index():
    Time = time.strftime("%H:%M:%S") # Current time
    return Time+" Serving from "+h_name+" ("+IP_addres+")\n"

if __name__ == '__main__':
    # Starting the server, listening on all interfaces (0.0.0.0) on port 5000
    app.run(host='0.0.0.0', port=5000)