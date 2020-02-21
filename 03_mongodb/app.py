from flask import Flask, jsonify, request, make_response
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongoadmin:mypassword@0.0.0.0:27017/testDatabase?authSource=admin"
mongo = PyMongo(app)


@app.route("/", methods=['GET'])
def home_page():
    db = mongo.db.users
    users = []
    for j in db.find():
        j.pop('_id')
        users.append(j)
    return jsonify(users)	


@app.route('/add/', methods=['POST']) #adding new item to bucketlist
def add_item():
	db = mongo.db.users
	user = {request}
	if db.find({'username' : "napoleone"}).count() > 0:
		return jsonify({"Message:" : "User Already Exists!"})
	else:
		db.insert(user)
		return jsonify({"Message:" : "User succesfully added!"})


if __name__ == '__main__':
    app.run(debug=True)
