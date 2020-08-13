
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    html = """
    <h1>안녕하세요<h1>
    """
    return html

datas = [45.7, 45, 10, 70.8]

@app.route('/signal')
def signal():
    global datas # global 변수인 것 명시
    datas.append( request.args.get("data") )
    return str(datas)

@app.route('/view')
def view():
    global datas # global 변수인 것 명시
    
    html = """
    """ + str(datas)
    return html


if __name__== '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)
