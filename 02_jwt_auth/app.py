from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

@app.route('/home')
def home():
    return ''

@app.route('/dashboard')
def dashboard():
    return ''

@app.route('/login')
def login():
    return ''

if __name__ == '__main__':
    app.run(debug=True)