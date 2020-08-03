
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    html = """
        <form action=/upload method=post enctype="multipart/form-data">
            <input type=file name=file1> <input type=submit value="전송">
            
        </form>
    """
    return html

@app.route('/upload', methods=["post"])
def upload():
    f = request.files["file1"]
    filename = "./static/" + f.filename
    f.save(filename)
    
    return "<img src=/static/" + f.filename + ">"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)
