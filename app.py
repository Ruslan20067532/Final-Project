from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import random

app = Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
jwt = JWTManager(app)

users = {
    "user1": "password123"
}

@app.route("/api/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    if username in users and users[username] == password:
        access_token = create_access_token(identity=username)
        return jsonify(token=access_token)
    return jsonify({"msg": "Bad credentials"}), 401

@app.route("/api/usage", methods=["GET"])
@jwt_required()
def get_usage():
    usage_data = [3.5, 4.2, 5.1, 2.7, 4.9, 6.0, 3.3]
    challenges = [
        "No social media for 2 hours",
        "Limit YouTube to 30 minutes",
        "No screens after 9 PM",
        "Take 3 walks today"
    ]
    return jsonify({
        "usage": usage_data,
        "challenge": random.choice(challenges)
    })

if __name__ == "__main__":
    app.run(debug=True)
