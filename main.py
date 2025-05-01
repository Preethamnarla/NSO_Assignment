import flask
import platform

app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n'


@app.route('/add')
def addition():
    value1=flask.request.args.get('A',default = 0, type = int)
    value2=flask.request.args.get('B',default = 0, type = int)
    result=value1+value2
    return '%d \n' % result


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8211,debug=True)
