from flask import request, jsonify
from flask_bcrypt import check_password_hash
from db import DB
from flask_jwt_extended import(
    jwt_required,
    create_access_token,
    get_jwt_identity
)

def login():
    # Get data from request
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    # Make the select query
    qry = "SELECT * FROM `users` WHERE `email` = :email"
    
    # Get user data from database
    print("Break3")
    user = DB.one(qry, {"email": email})
    # Check if user exists and hashed password matches
    if not user or not check_password_hash(user["password"], password):
        return{"message": "invalid credentials"}, 401

    # Delete password
    del user["password"]

    # Create JWT
    access_token = create_access_token(user)
    return jsonify(access_token = access_token, message = "success"), 200

#User needs to be logged in for this route
@jwt_required()
def me():
    user = get_jwt_identity()
    return jsonify(user=user, message = "success"), 200