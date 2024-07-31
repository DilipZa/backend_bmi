from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/calculate',methods=['POST'])
def cal_bmi():
    data = request.get_json()
    weight = float(data['weight'])
    height = float(data['height'])
    bmi = weight/(height ** 2)
    return  jsonify(bmi)

@app.route('/')
def Greet():
    return "Welcome"

@app.route('/greet_user')
def greet_user():
    return "Welcome Dilip !!"

if __name__ == '__main__':
    app.run(debug=True)