from flask import Flask, jsonify, request, make_response
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY'] = 'sopralapancalacapracanta'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token') # http://127.0.0.1:5000/route?token=kjfkjgkfjgkfdjgkdf
        if not token:
            return jsonify({'message' : 'Token non presente'}), 403

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        
        except:
            return jsonify({'message' : 'Token non valido'}), 403
        
        return f(*args, **kwargs)
    
    return decorated


@app.route('/home')
def home():
    return jsonify({'message' : 'tutti mi possono vedere'})


@app.route('/dashboard')
@token_required
def dashboard():
    return jsonify({'message' : 'area riservata'})


@app.route('/login')
def login():
    auth = request.authorization

    if auth and auth.password == 'password':
        token = jwt.encode({'user' : auth.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'token' : token.decode('UTF-8')})

    return make_response('Non posso verificare la passord', 401, {'WWW-Authenticate' : 'Basic real="Password Required"'})


if __name__ == '__main__':
    app.run(debug=True)