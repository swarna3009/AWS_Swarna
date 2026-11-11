from flask import Flask,request,jsonify
from swarna import get_names
app = Flask(__name__)
@app.route('/')
def hello():
    return "hello world"
@app.route('/api',methods=["GET"])
def api():
    data = get_names()
    data ={
        'data':data
    }
    return jsonify(data)
if __name__ == '__main__':
    app.run(port=8000,host='0.0.0.0',debug =True)


